from fastapi import FastAPI, UploadFile, File, HTTPException
import os
from app.loader import load_pdf

app = FastAPI()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "RAG Resume Assistant running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # ✅ Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        text = load_pdf(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not text.strip():
        raise HTTPException(status_code=400, detail="No readable text found in PDF")

    return {
        "filename": file.filename,
        "text_preview": text[:500]
    }