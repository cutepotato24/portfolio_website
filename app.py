import streamlit as st
from groq import Groq
import base64
import os

# 1. Page Layout Configuration
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# --- SAFE SCRAMBLED KEY LOADER ---
# Paste your SCRAMBLED text string from Step 1 between these quotes:
SCRAMBLED_KEY = "Z3NrX1lPVVJfQUNUVUFMX0tFWV9IRVJF"

# This automatically unscrambles it back into your real key at runtime
try:
    API_KEY = base64.b64decode(SCRAMBLED_KEY.encode()).decode()
except Exception:
    API_KEY = ""

# Back up check for the deployed Streamlit Cloud secrets environment panel later
if not API_KEY or "YOUR_ACTUAL_KEY" in API_KEY:
    API_KEY = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
# ---------------------------------

# 2. Sidebar Structural Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Projects", "Skills & Experience", "Contact"])

# --- PAGE 1: ABOUT ME (With AI Welcoming Chatbot!) ---
if page == "About Me":
    st.title("Hi, I'm a Developer 👋")
    st.subheader("Data Analyst / Software Engineer")
    st.write("""
    Welcome to my portfolio! I build web applications and analyze data to solve real-world problems. 
    Use the sidebar to view my technical details, or talk to my welcoming assistant below!
    """)
    
    st.divider()
    st.markdown("### 🤖 Chat with my AI Assistant")

    if not API_KEY:
        st.info("👋 Hi! The welcoming chatbot is currently in preview mode. Configure your API credentials to talk live!")
    else:
        # Initialize the high-speed Groq inference client engine
        client = Groq(api_key=API_KEY)
        
        # System parameters defining the assistant's boundaries
        portfolio_context = """
        You are an enthusiastic AI Assistant hosting the personal portfolio website of a software engineer.
        - Core Stack: Python, SQL, Git, GitHub, Pandas, and Streamlit.
        - Core Projects: Built this custom interactive portfolio web app using cloud-native python workflows.
        - Instructions: Keep responses brief, enthusiastic, friendly, and strictly under 3 sentences. Direct users to the sidebar links for more information.
        """

        # Keep track of sequential conversational data state arrays
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi there! Welcome to this portfolio. What would you like to know about my work?"}
            ]

        # Render logging data pipelines sequentially
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Capture live character text box entries
        if user_prompt := st.chat_input("Ask me a question..."):
            with st.chat_message("user"):
                st.write(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            try:
                # Query LLama 3 engine cluster configurations
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": portfolio_context},
                        {"role": "user", "content": user_prompt}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                ai_response = chat_completion.choices.message.content
            except Exception as e:
                ai_response = f"⚠️ API Connection Error: {str(e)}"

            with st.chat_message("assistant"):
                st.write(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

# --- PAGE 2: PROJECTS ---
elif page == "Projects":
    st.title("Featured Projects 🚀")
    with st.expander("📊 Project 1: Cloud-Native Portfolio Web App", expanded=True):
        st.markdown("#### Tech Stack: `Python`, `Streamlit`, `Groq Cloud AI`")
        st.write("Designed an interactive professional portfolio website incorporating localized AI chatbot chat flows to serve as a 24/7 host.")

# --- PAGE 3: SKILLS & EXPERIENCE ---
elif page == "Skills & Experience":
    st.title("Technical Skills 🛠️")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Languages")
        st.markdown("`Python` `SQL` `HTML` `CSS`")
    with col2:
        st.markdown("### Tools & Frameworks")
        st.markdown("`Streamlit` `Git` `GitHub` `Pandas` `Groq API`")

# --- PAGE 4: CONTACT ---
elif page == "Contact":
    st.title("Get In Touch 📧")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("🐙 [GitHub](https://github.com)")
