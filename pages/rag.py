
import streamlit as st
import requests

st.set_page_config(page_title="🧠 RAG Assistant", page_icon="🤖")
st.title("🤖 RAG Assistant")

# Require login
if "user_id" not in st.session_state:
    st.warning("🔐 Please log in on the Home page first.")
    st.stop()

API_BASE = "https://hacksub-production.up.railway.app"
UPLOAD_URL = f"{API_BASE}/upload"
CHAT_URL   = f"{API_BASE}/chat"

# --- Upload Section ---
st.subheader("📤 Upload a PDF")
uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
if uploaded_file and st.button("Upload PDF"):
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    data  = {"user_id": st.session_state["user_id"]}

    try:
        resp = requests.post(UPLOAD_URL, files=files, data=data)
        if resp.ok:
            st.success(f"Uploaded! Chunks: {resp.json().get('chunks')}")
        else:
            st.error(f"Upload failed: {resp.text}")
    except Exception as e:
        st.error(f"🚨 Error: {e}")

# --- Chat Section ---
st.subheader("💬 Ask a Question")
query = st.text_area("Enter your question:")
if query and st.button("Send Question"):
    payload = {"question": query}
    try:
        resp = requests.post(CHAT_URL, json=payload)
        if resp.ok:
            answer = resp.json().get("answer", "<no answer>")
            st.markdown(f"**Answer:** {answer}")
        else:
            st.error(f"Chat error: {resp.text}")
    except Exception as e:
        st.error(f"🚨 Error: {e}")
