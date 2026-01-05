import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Chatbot", layout="centered")

st.title("🤖 Simple Gemini Chatbot")

# Get API key from Streamlit Secrets
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found in Streamlit Secrets")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Valid model
model = genai.GenerativeModel("models/gemini-1.5-flash")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input.strip():
        response = model.generate_content(user_input)
        st.write("**Gemini Reply:**")
        st.write(response.text)
    else:
        st.warning("Please type a question")
