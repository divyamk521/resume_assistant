# 🧠 RAG Resume Assistant

An end-to-end **Retrieval-Augmented Generation (RAG)** system that allows recruiters to intelligently query candidate resumes using AI.

---

## 🚀 Features

- 📄 Upload and process PDF resumes
- 🔍 Semantic search using vector embeddings
- 🧠 Context-aware answers powered by LLM (Groq)
- 💬 Chat-based interface (Streamlit UI)
- ⚡ FastAPI backend for efficient processing

---

## 🏗️ Tech Stack

- **Backend:** FastAPI  
- **LLM:** Groq (LLaMA 3.1)  
- **RAG Framework:** LangChain  
- **Vector DB:** FAISS  
- **Embeddings:** Sentence Transformers  
- **Frontend/UI:** Streamlit  

---

## 🔄 How It Works (RAG Pipeline)

1. 📄 Upload Resume (PDF)
2. 🧾 Extract text from document
3. ✂️ Split text into chunks
4. 🔢 Convert chunks into embeddings
5. 📦 Store embeddings in FAISS vector database
6. 🔍 Retrieve relevant chunks for a query
7. 🤖 Generate final answer using LLM

---

## 💬 Demo Flow

1. Upload a resume  
2. Ask questions like:
   - *"What skills does this candidate have?"*
   - *"What projects has the candidate worked on?"*
3. Get accurate, context-aware answers instantly  

---

## 📦 API Endpoints

### ➤ Upload Resume

POST /upload


### ➤ Query Resume

POST /query


#### Example Request
```json
{
  "question": "What skills does the candidate have?"
}

⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/rag-resume-assistant.git
cd rag-resume-assistant
2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token (optional)
4. Run Backend (FastAPI)
uvicorn app.main:app --reload
5. Run UI (Streamlit)
streamlit run streamlit_app.py

🧠 Use Cases
📊 Resume screening for recruiters
🎯 Candidate evaluation
⚡ Quick skill extraction
🤖 AI-powered HR assistant
💡 Key Highlights
Built a complete RAG pipeline from scratch
Uses semantic search instead of keyword matching
Separates retrieval and generation for accuracy
Designed with real-world recruiter use case

📌 Future Improvements
📁 Multi-resume comparison
📊 Candidate ranking system
🌍 Deployment (cloud + Docker)
🎨 Enhanced UI/UX
👤 Author

Divya M K
Python Backend Developer | FastAPI | AI Applications