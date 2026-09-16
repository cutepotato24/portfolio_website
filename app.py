import streamlit as st
from google import genai
import os

# 1. Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# 2. Secure API Key Initialization
# Locally: Looks inside your system environment or Streamlit secrets
# Streamlit Cloud: Reads from the dashboard's "Secrets" configuration
API_KEY = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    st.warning("⚠️ Please configure your GEMINI_API_KEY to activate the welcoming chatbot.")

# 3. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Projects", "Skills & Experience", "Contact"])

# --- PAGE 1: ABOUT ME (With AI Welcoming Bot!) ---
if page == "About Me":
    st.title("Hi, I'm a Developer 👋")
    st.subheader("Data Analyst / Software Engineer")
    st.write("Welcome to my portfolio! I build web applications and analyze data to solve problems.")
    
    st.divider()
    st.markdown("### 🤖 Chat with my AI Assistant")

    if API_KEY:
        # Initialize the official Gemini Client
        client = genai.Client(api_key=API_KEY)
        
        # Set a hardcoded context profile for the bot to read from
        portfolio_context = """
        You are a welcoming, enthusiastic AI Assistant hosting the personal portfolio website of 'Alex'.
        Here are Alex's details:
        - Role: Data Analyst and Software Engineer specializing in Python, SQL, and Streamlit.
        - Core Projects: Built a custom interactive portfolio web app (this site) and an upcoming machine learning engine.
        - Call to Action: Direct users to look at the 'Projects' tab for source code, or the 'Contact' tab to reach out on LinkedIn.
        Keep answers friendly, professional, concise, and under 3 sentences. Do not hallucinate fields Alex does not know.
        """

        # Initialize Chat History for the web interface
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi there! I am Alex's AI assistant. Ask me anything about their work!"}
            ]

        # Display history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Handle Live Inputs via Gemini
        if user_prompt := st.chat_input("Ask a question about Alex..."):
            with st.chat_message("user"):
                st.write(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            # Send prompt to Gemini with system parameters
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",  # Fast, highly optimized free-tier model
                    contents=user_prompt,
                    config={"system_instruction": portfolio_context}
                )
                ai_response = response.text
            except Exception as e:
                ai_response = f"Sorry, I had trouble processing that request right now."

            with st.chat_message("assistant"):
                st.write(ai_response)
                
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

# --- PAGE 2, 3, 4 (Keep your existing structural pages the same) ---
elif page == "Projects":
    st.title("Featured Projects 🚀")
elif page == "Skills & Experience":
    st.title("Technical Skills 🛠️")
elif page == "Contact":
    st.title("Get In Touch 📧")
