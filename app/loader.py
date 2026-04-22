from pypdf import PdfReader
from pypdf.errors import PdfReadError

def load_pdf(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    except Exception as e:
        raise ValueError(f"Error reading PDF: {str(e)}")