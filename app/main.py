from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from app.loader import load_pdf
from app.rag_pipeline import chunk_text, create_vector_store, generate_answer

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "data"
VECTORSTORE_DIR = "vectorstore"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTORSTORE_DIR, exist_ok=True)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "RAG Resume Assistant running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
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

    chunks = chunk_text(text)
    vectorstore = create_vector_store(chunks)
    vectorstore.save_local(VECTORSTORE_DIR)

    return {"message": "Resume processed successfully"}


@app.post("/query")
def query_rag(request: QueryRequest):
    try:
        answer = generate_answer(request.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "question": request.question,
        "answer": answer
    }