# 🩺 MedPal

**MedPal** is your personal medical buddy. Don't know where to save medical reports or how to understand them? Don’t worry — we got you.

MedPal simplifies complex medical jargon into easy-to-understand summaries. It checks whether your medical values fall within normal ranges and suggests actionable next steps, helping you seek timely assistance from medical professionals. It also lets you query your uploaded reports using Retrieval-Augmented Generation (RAG).


## [Live Website](https://medpal.streamlit.app/)
## [Demo Vid]()
---

## 💡 Inspiration

We noticed how overwhelming medical reports can be — full of jargon, numbers, and reference ranges that aren’t easy to interpret. People often have no idea what to do after receiving lab results. We wanted to create something that not only stores reports but also makes sense of them, offering guidance in plain language.

---

## ⚙️ What It Does

MedPal allows users to:

- 📄 Upload medical PDF reports  
- 🧠 Extract and analyze medical data  
- 🔍 Check whether values fall within normal ranges  
- 💬 Ask questions like “Is my blood sugar level normal?”  
- 🗒️ Receive suggestions like “Consult a cardiologist”  
- 🔎 Search and ask questions about previously uploaded reports using RAG  

All of this is powered by a Retrieval-Augmented Generation (RAG) pipeline integrated with embeddings and an LLM.

---

## 🛠️ Tech Stack

**Frontend**  
- Streamlit – For user authentication, PDF uploads, and chat interface  

**Backend**  
- FastAPI – For handling uploads and serving LLM responses  
- Cohere – For generating text embeddings  
- Qdrant – As the vector database for storing PDF chunks  
- Groq – For running the LLM and generating smart responses  
[I'm Backend](https://github.com/ZehraArshad/Hack_Sub)
---

## 🚀 How It Works

1. 🔐 Sign in with Google  
2. 📤 Upload a medical PDF file  
3. 💬 Ask questions about your report using RAG  
