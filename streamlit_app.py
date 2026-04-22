import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="RAG Resume Assistant",
    page_icon="🧠",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
        .main {
            padding-top: 1rem;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stChatMessage {
            border-radius: 12px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 RAG Resume Assistant")
st.caption("Ask intelligent questions about any resume using AI")

# Sidebar
with st.sidebar:
    st.header("📄 Upload Resume")

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        st.success(f"Selected: {uploaded_file.name}")

        if st.button("Upload Resume"):
            with st.spinner("Processing resume..."):
                files = {
                    "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
                }

                res = requests.post("http://127.0.0.1:8000/upload", files=files)

                if res.status_code == 200:
                    st.success("✅ Resume processed successfully!")
                    st.session_state["uploaded"] = True
                else:
                    st.error("❌ Upload failed")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["text"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["text"])

# Input box
question = st.chat_input("Ask something about the resume...")

if question:
    st.session_state.messages.append({"role": "user", "text": question})

    with st.spinner("Thinking..."):
        try:
            res = requests.post(
                "http://127.0.0.1:8000/query",
                json={"question": question},
            )

            if res.status_code == 200:
                answer = res.json()["answer"]
            else:
                answer = "❌ Error getting response"

        except:
            answer = "❌ Backend not running"

    st.session_state.messages.append({"role": "assistant", "text": answer})
    st.rerun()