import streamlit as st
from pymongo import MongoClient
import base64
from datetime import datetime
from bson.binary import Binary
from pymongo.server_api import ServerApi
import base64


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

    st.download_button(
        label="📥 Download PDF",
        data=doc["file"],
        file_name=doc['filename'],
        mime="application/pdf"
    )

    st.markdown("---")
    # st.markdown("OR view it below:")

    # base64_pdf = base64.b64encode(doc["file"]).decode("utf-8")

    # st.components.v1.html(f"""
    #     <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px"></iframe>
    # """, height=650)

    # st.markdown("---")