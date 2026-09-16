import streamlit as st
from groq import Groq
import os

# 1. Page Setup
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# 2. Secure API Key Broker
# When live on the web: Reads from Streamlit Cloud's built-in secure vault
# When testing in Codespaces: Reads from the fallback variable below
API_KEY = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")

# 💡 LOCAL TESTING ONLY: If your chatbot says it's missing a key, paste your key between the quotes here:
# WARNING: Remove your key from the line below before pushing to GitHub to prevent blocks!
LOCAL_TEST_KEY = "" 

if not API_KEY and LOCAL_TEST_KEY:
    API_KEY = LOCAL_TEST_KEY

# 3. Sidebar Navigation Layout
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
        st.info("👋 Hi! The welcoming chatbot is currently in preview mode. Paste your Groq API key inside the code or Streamlit secrets panel to start conversing live!")
    else:
        # Initialize the free Groq engine
        client = Groq(api_key=API_KEY)
        
        # Give the AI assistant a persona rulesheet
        portfolio_context = """
        You are an enthusiastic AI Assistant hosting the personal portfolio website of a software engineer.
        - Core Stack: Python, SQL, Git, GitHub, Pandas, and Streamlit.
        - Core Projects: Built this custom interactive portfolio web app using cloud-native python workflows.
        - Instructions: Keep responses brief, enthusiastic, friendly, and strictly under 3 sentences. Direct users to the sidebar links for more information.
        """

        # Maintain chat history state
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi there! Welcome to this portfolio. What would you like to know about my work?"}
            ]

        # Display structural history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Process message inputs
        if user_prompt := st.chat_input("Ask me a question..."):
            with st.chat_message("user"):
                st.write(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": portfolio_context},
                        {"role": "user", "content": user_prompt}
                    ],
                    model="llama-3.3-70b-versatile",
                )
                ai_response = chat_completion.choices.message.content
            except Exception as e:
                ai_response = "Sorry, I ran into a connection glitch. Please try messaging me again in a moment!"

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
