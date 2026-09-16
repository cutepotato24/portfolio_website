import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My Portfolio", 
    page_icon="💼", 
    layout="centered"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Projects", "Skills & Experience", "Contact"])

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
    st.write("Here are some projects I have worked on:")

    with st.expander("📊 Project 1: Portfolio Web App", expanded=True):
        st.write("**Tech Stack:** Python, Streamlit, GitHub")
        st.write("Created an interactive, cloud-deployed professional portfolio website to showcase my coding journey.")

    with st.expander("🤖 Project 2: Coming Soon..."):
        st.write("Stay tuned! I am actively working on new data and development projects.")

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
    st.write("Feel free to connect with me on social media or check out my repositories.")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("🐙 [GitHub](https://github.com)")
