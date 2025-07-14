import streamlit as st
from streamlit_oauth import OAuth2Component
import requests

# === Config ===
client_id = st.secrets["google"]["client_id"]
client_secret = st.secrets["google"]["client_secret"]
redirect_uri = "http://localhost:8501"  # later: your deployed URL

# === OAuth Component ===
oauth2 = OAuth2Component(
    client_id=client_id,
    client_secret=client_secret,
    authorize_endpoint="https://accounts.google.com/o/oauth2/v2/auth",
    token_endpoint="https://oauth2.googleapis.com/token"
)

# === UI ===
st.set_page_config(page_title="MedPal", page_icon="🩺")
st.title("🩺 MedPal PDF Assistant")

result = oauth2.authorize_button(
    name="Continue with Google",
    redirect_uri=redirect_uri,
    scope="openid email profile",
    key="google",
    extras_params={"access_type": "offline"},
)

# === After Login ===
if result:
    
    if "token" in result and "access_token" in result["token"]:
        access_token = result["token"]["access_token"]

        user_info = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        st.session_state["user_id"] = user_info["id"]
        st.session_state["email"] = user_info["email"]
        st.success(f"✅ Logged in as: {user_info['email']} with User Id: {user_info['id']}")

        # 👉 Now you can show upload/chat/dashboard here
            # === Upload Section ===
        st.subheader("📤 Upload PDF")
        uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
        if uploaded_file and st.button("Upload"):
            files = {"file": uploaded_file}
            data = {"user_id": st.session_state["user_id"]}
            try:
                response = requests.post("https://your-backend-url/upload", files=files, data=data)
                if response.status_code == 200:
                    st.success("✅ Upload successful!")
                else:
                    st.error(f"Upload failed: {response.text}")
            except Exception as e:
                st.error(f"❌ Error: {e}")

        # === Chat Section ===
        st.subheader("💬 Ask a Question")
        query = st.text_area("Enter your question")
        if st.button("Ask"):
            payload = {"question": query}
            try:
                response = requests.post("https://your-backend-url/chat", json=payload)
                if response.status_code == 200:
                    st.markdown(f"**Answer:** {response.json()['answer']}")
                else:
                    st.error(f"Chat failed: {response.text}")
            except Exception as e:
                st.error(f"❌ Error: {e}")

    else:
        st.warning("🔐 Waiting for Google authorization... Please complete login.")


    # ...rest of your app logic...


else:
    st.info("👆 Please log in with Google to continue.")
