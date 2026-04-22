from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from app.embeddings import get_embedding_model
from app.config import GROQ_API_KEY
from groq import Groq


def chunk_text(text: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    documents = text_splitter.create_documents([text])
    return documents


def create_vector_store(documents):
    embedding_model = get_embedding_model()
    vectorstore = FAISS.from_documents(documents, embedding_model)
    return vectorstore


def load_vector_store():
    embedding_model = get_embedding_model()
    vectorstore = FAISS.load_local(
        "vectorstore",
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return vectorstore


def retrieve_chunks(query: str):
    vectorstore = load_vector_store()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)
    return docs


def generate_answer(query: str):
    docs = retrieve_chunks(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt_template = """
You are an expert recruiter assistant.

Your task is to analyze a candidate's resume and answer questions accurately.

Instructions:
- Use ONLY the provided context
- Be concise and structured
- Highlight key skills, tools, and experience clearly
- If information is missing, say "Not mentioned in resume"

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = PromptTemplate.from_template(prompt_template)

    final_prompt = prompt.format(
        context=context,
        question=query
    )

    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": final_prompt}
        ]
    )

    return response.choices[0].message.content