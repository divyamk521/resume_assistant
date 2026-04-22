# 🧠 RAG Resume Assistant

An end-to-end Retrieval-Augmented Generation (RAG) system that allows recruiters to query candidate resumes intelligently.

## 🚀 Features

- Upload PDF resumes
- Extract and process text
- Semantic search using embeddings
- Context-aware answers using LLM (Groq)
- FastAPI backend for API access

## 🏗️ Tech Stack

- FastAPI
- LangChain
- FAISS (Vector Database)
- Sentence Transformers (Embeddings)
- Groq API (LLM)

## 🔄 Pipeline

1. Upload Resume (PDF)
2. Extract Text
3. Chunk Text into Documents
4. Generate Embeddings
5. Store in FAISS Vector DB
6. Retrieve Relevant Chunks
7. Generate Answer using LLM

## 📦 API Endpoints

### Upload Resume
POST /upload

### Ask Question
POST /query

Example:
```json
{
  "question": "What skills does the candidate have?"
}


Setup
git clone https://github.com/YOUR_USERNAME/rag-resume-assistant.git
cd rag-resume-assistant
pip install -r requirements.txt

Create .env:

GROQ_API_KEY=your_key
HF_TOKEN=your_token (optional)

Run:

uvicorn app.main:app --reload


🧠 Use Cases:

Recruiter resume screening
Candidate evaluation
Quick skill extraction

📌 Future Improvements:

UI (React frontend)
Multi-document support
Ranking improvements
Deployment (Docker + cloud)


👤 Author:
Divya M K