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
st.markdown("<h1 style='margin-bottom: 10px;'>🩺 MedPal PDF Assistant</h1>", unsafe_allow_html=True)
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
        st.success(f"✅ Logged in as: {user_info['email']}")

        # === Header Bar ===
        col1, col2, col3 = st.columns([4, 4, 2])
        with col1:
            st.write(f"👤 **User ID:** `{st.session_state['user_id']}`")
        with col2:
            st.write(f"📧 **Email:** `{st.session_state['email']}`")
            # 👉 Now you can show upload/chat/dashboard here
            # === Upload Section ===
        
        
    else:
        st.warning("🔐 Waiting for Google authorization... Please complete login.")


    # ...rest of your app logic...


else:
    st.info("👆 Please log in with Google to continue.")
