import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(
    page_title="My Portfolio", 
    page_icon="💼", 
    layout="centered"
)

# 2. Sidebar Navigation (Added "AI Chatbot" as an option)
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:", 
    ["About Me", "Projects", "Skills & Experience", "AI Chatbot", "Contact"]
)

# --- PAGE 1: ABOUT ME ---
if page == "About Me":
    st.title("Hi, I'm a Developer 👋")
    st.subheader("Data Analyst / Software Engineer")
    st.write("""
    Welcome to my portfolio! I build web applications and analyze data to solve real-world problems. 
    Explore this site using the sidebar navigation to see my projects, skills, and how to get in touch.
    """)
    st.divider()
    st.markdown("### Quick Facts")
    st.write("- 💻 Passionate about Python, automation, and web development")
    st.write("- 🚀 Constant learner looking for exciting new opportunities")

# --- PAGE 2: PROJECTS ---
elif page == "Projects":
    st.title("Featured Projects 🚀")
    with st.expander("📊 Project 1: Portfolio Web App", expanded=True):
        st.write("**Tech Stack:** Python, Streamlit, GitHub")
        st.write("Created an interactive, cloud-deployed professional portfolio website.")

# --- PAGE 3: SKILLS & EXPERIENCE ---
elif page == "Skills & Experience":
    st.title("Technical Skills 🛠️")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Languages")
        st.markdown("`Python` `SQL` `HTML` `CSS`")
    with col2:
        st.markdown("### Frameworks & Tools")
        st.markdown("`Streamlit` `Git` `GitHub` `Pandas`")

# --- PAGE 4: AI CHATBOT (New Section!) ---
elif page == "AI Chatbot":
    st.title("🤖 Chat with my AI Assistant")
    st.write("Ask me anything about my projects, skills, or background!")

    # Initialize Chat History for this session
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi there! I am your host's AI assistant. How can I help you today?"}
        ]

    # Display previous conversation history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Handle New User Input
    if user_prompt := st.chat_input("Ask me a question..."):
        with st.chat_message("user"):
            st.write(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Generate Assistant Response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Simple mock keyword routing for portfolio answers
            user_lower = user_prompt.lower()
            if "project" in user_lower:
                assistant_response = "I have built a custom portfolio web app using Python and Streamlit, which you can check out in the Projects tab!"
            elif "skill" in user_lower or "tech" in user_lower or "python" in user_lower:
                assistant_response = "I specialize in Python, SQL, Git, and data manipulation tools like Pandas."
            elif "contact" in user_lower or "email" in user_lower or "hire" in user_lower:
                assistant_response = "You can reach out directly via the Contact page or connect with me on LinkedIn!"
            else:
                assistant_response = "That is a great question! Feel free to explore the sidebar options to learn more about my background, or head to the Contact page to drop a line."

            # Simulate typing animation effect
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
                
            message_placeholder.markdown(full_response)
            
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- PAGE 5: CONTACT ---
elif page == "Contact":
    st.title("Get In Touch 📧")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("🐙 [GitHub](https://github.com)")
