import streamlit as st
from groq import Groq

# Page config
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")

# Create Groq client using Streamlit Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🤖 Simple Groq Chatbot")

# Input box
user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input.strip():
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",   # ✅ Supported Groq model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=512
            )

            st.markdown("### 💬 Groq Reply:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error("❌ Groq API Error")
            st.exception(e)
    else:
        st.warning("⚠️ Please type a question.")
