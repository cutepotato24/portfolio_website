import streamlit as st
from groq import Groq
import os

# 1. Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# 2. Secure API Key Initialization (Looking for GROQ_API_KEY now)
API_KEY = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")

if not API_KEY:
    st.warning("⚠️ Please configure your GROQ_API_KEY to activate the welcoming chatbot.")

# 3. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Projects", "Skills & Experience", "Contact"])

# --- PAGE 1: ABOUT ME (With Groq Welcoming Bot!) ---
if page == "About Me":
    st.title("Hi, I'm a Developer 👋")
    st.subheader("Data Analyst / Software Engineer")
    st.write("Welcome to my portfolio! I build web applications and analyze data to solve problems.")
    
    st.divider()
    st.markdown("### 🤖 Chat with my AI Assistant")

    if API_KEY:
        # Initialize the free Groq client
        client = Groq(api_key=API_KEY)
        
        # Hardcoded context profile for the bot to read from
        portfolio_context = """
        You are a welcoming, enthusiastic AI Assistant hosting the personal portfolio website of 'Alex'.
        Here are Alex's details:
        - Role: Data Analyst and Software Engineer specializing in Python, SQL, and Streamlit.
        - Core Projects: Built a custom interactive portfolio web app (this site) and an upcoming machine learning engine.
        - Call to Action: Direct users to look at the 'Projects' tab for source code, or the 'Contact' tab to reach out on LinkedIn.
        Keep answers friendly, professional, concise, and under 3 sentences. Do not make up info Alex does not know.
        """

        # Initialize Chat History
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi there! I am Alex's AI assistant. Ask me anything about their work!"}
            ]

        # Display history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Handle Live Inputs via Groq
        if user_prompt := st.chat_input("Ask a question about Alex..."):
            with st.chat_message("user"):
                st.write(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            # Send prompt to Groq with system context
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": portfolio_context},
                        {"role": "user", "content": user_prompt}
                    ],
                    model="llama-3.3-70b-versatile", # Incredibly fast and completely free
                )
                ai_response = chat_completion.choices[0].message.content
            except Exception as e:
                ai_response = "Sorry, I had trouble processing that request right now."

            with st.chat_message("assistant"):
                st.write(ai_response)
                
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

# --- KEEPING OTHER PAGES THE SAME ---
elif page == "Projects":
    st.title("Featured Projects 🚀")
elif page == "Skills & Experience":
    st.title("Technical Skills 🛠️")
elif page == "Contact":
    st.title("Get In Touch 📧")
