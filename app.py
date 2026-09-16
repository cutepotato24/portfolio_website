import streamlit as st
from groq import Groq
import os

st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# --- DEBUGGING KEY RESOLUTION ---
# Attempt to read from Streamlit's secrets, fallback to terminal export environment
API_KEY = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")

# Hardcoded test fallback (Only if both files fail to load in Codespaces)
if not API_KEY:
    # If secrets file isn't reading, you can temporarily hardcode it here just to test:
    # API_KEY = "gsk_your_actual_key" 
    pass

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Projects", "Skills & Experience", "Contact"])

if page == "About Me":
    st.title("Hi, I'm a Developer 👋")
    st.write("Welcome to my portfolio! Let's talk to my AI assistant.")
    st.divider()
    
    # If the key isn't found, show this helper error
    if not API_KEY:
        st.error("❌ App cannot connect to Groq because GROQ_API_KEY is completely empty inside Streamlit context.")
    else:
        # Initialize Groq
        client = Groq(api_key=API_KEY)
        
        # System persona context instructions
        portfolio_context = "You are a professional assistant for a developer's portfolio."

        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Hi! Ask me anything about my work."}]

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Chat interface trigger
        if user_prompt := st.chat_input("Ask a question..."):
            with st.chat_message("user"):
                st.write(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            try:
                # Making the explicit API post
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": portfolio_context},
                        {"role": "user", "content": user_prompt}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                ai_response = chat_completion.choices[0].message.content
            except Exception as e:
                # Capture the exact error signature from Groq's servers
                ai_response = f"⚠️ Groq API Error: {str(e)}"

            with st.chat_message("assistant"):
                st.write(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
