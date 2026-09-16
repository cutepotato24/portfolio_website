import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="My Portfolio", 
    page_icon="💼", 
    layout="centered"
)

# 2. Sidebar Navigation (Removed "AI Chatbot" from options)
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:", 
    ["About Me", "Projects", "Skills & Experience", "Contact"]
)

# --- PAGE 1: ABOUT ME (With Welcoming Bot!) ---
if page == "About Me":
    st.title("Hi, I'm a Developer 👋")
    st.subheader("Data Analyst / Software Engineer")
    
    st.write("""
    Welcome to my portfolio! I build web applications and analyze data to solve real-world problems. 
    Use the sidebar to view my technical details, or talk to my welcoming assistant below!
    """)
    
    st.divider()
    
    # --- WELCOMING CHATBOT SECTION ---
    st.markdown("### 🤖 Chat with my AI Assistant")
    st.caption("Ask me about my background, skills, or projects!")

    # Initialize Chat History for this session if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi there! Welcome to this portfolio. Ask me anything about my work!"}
        ]

    # Display previous conversation history inside a neat container
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # Handle New User Input
    if user_prompt := st.chat_input("Ask a question..."):
        # Display user message
        with chat_container.chat_message("user"):
            st.write(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Generate Assistant Response
        with chat_container.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Simple keyword matching responses
            user_lower = user_prompt.lower()
            if "project" in user_lower:
                assistant_response = "I have built several projects including this web portfolio. Head over to the 'Projects' tab in the sidebar to see them all!"
            elif "skill" in user_lower or "tech" in user_lower or "python" in user_lower:
                assistant_response = "I specialize in Python, SQL, Git, and data frameworks like Pandas. Check the 'Skills & Experience' tab for a full breakdown."
            elif "contact" in user_lower or "email" in user_lower or "hire" in user_lower:
                assistant_response = "You can easily reach out to me! Just click on the 'Contact' tab in the sidebar for my LinkedIn and GitHub links."
            else:
                assistant_response = "Thanks for asking! You can explore the tabs on the left sidebar to learn more details about my journey."

            # Simulate typing animation effect
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.04)
                message_placeholder.markdown(full_response + "▌")
                
            message_placeholder.markdown(full_response)
            
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    # ----------------------------------

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

# --- PAGE 4: CONTACT ---
elif page == "Contact":
    st.title("Get In Touch 📧")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("🐙 [GitHub](https://github.com)")
