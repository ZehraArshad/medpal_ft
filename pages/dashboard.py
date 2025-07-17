import streamlit as st
from pymongo import MongoClient
import base64
from datetime import datetime
from bson.binary import Binary
from pymongo.server_api import ServerApi


# Assuming DB and collection are already set up
uri = st.secrets['mongodb']['uri']
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["medpal_db"]
collection = db["user_uploads"]
st.title("📄 Your Uploaded Medical PDFs")

user_id = st.session_state.get("user_id")  # Must be set earlier (e.g. during login)

if not user_id:
    st.warning("⚠️ You must be logged in to view this page.")
    st.stop()

docs = collection.find({"user_id": user_id}).sort("upload_time", -1)

for doc in docs:
    st.markdown(f"**📎 Filename:** {doc['filename']}")
    st.markdown(f"🕒 Uploaded on: `{doc['upload_time'].strftime('%Y-%m-%d %H:%M:%S')}`")

    # Convert binary to base64
    pdf_bytes = doc["file"]
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    # Streamlit's built-in PDF viewer using iframe
    pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.markdown("---")
