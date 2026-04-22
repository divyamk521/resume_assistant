import streamlit as st
import requests

st.set_page_config(page_title="RAG Resume Assistant", layout="wide")

st.title("🧠 RAG Resume Assistant")

# Upload section
st.subheader("Upload Resume")

uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

if uploaded_file is not None:
    if st.button("Upload"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/upload", files=files)

        if response.status_code == 200:
            st.success("Resume uploaded successfully!")
        else:
            st.error("Upload failed")

# Chat section
st.subheader("Ask Questions")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["text"])
    else:
        st.chat_message("assistant").write(msg["text"])

# Input
question = st.chat_input("Ask something about the resume...")

if question:
    st.session_state.messages.append({"role": "user", "text": question})

    with st.spinner("Thinking..."):
        response = requests.post(
            "http://127.0.0.1:8000/query",
            json={"question": question},
        )

        if response.status_code == 200:
            answer = response.json()["answer"]
        else:
            answer = "Error getting response"

    st.session_state.messages.append({"role": "assistant", "text": answer})
    st.rerun()