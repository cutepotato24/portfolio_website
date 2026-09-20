import streamlit as st

# 1. Page Configuration (Must be the first command)
st.set_page_config(
    page_title="Professional Portfolio", 
    page_icon="💼", 
    layout="centered"
)

# 2. Sidebar Structural Navigation
st.sidebar.markdown("## 🧭 Navigation")
page = st.sidebar.radio("Go to:", ["Profile Overview", "Core Projects", "Technical Skills", "Contact & Links"])

# --- PAGE 1: PROFILE OVERVIEW ---
if page == "Profile Overview":
    st.title("Hi, I'm Harold, how are you today? 👋")
    st.subheader("Analytics & Software Engineer")
    
    # Highlight Banner
    st.info("🚀 Specialized in building automated data workflows and clean user experiences.")
    
    st.markdown("### 🎯 Professional Profile")
    st.write("""
    I am a results-driven professional dedicated to transforming complex data sets into clear, actionable business strategies. 
    By leveraging cloud-native python workflows, I design and implement reliable pipeline structures that help organizations scale.
    """)
    
    st.divider()
    st.markdown("### 📊 Career Statistics")
    
    # Modern metrics display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Python Projects", value="12+", delta="Active")
    with col2:
        st.metric(label="Data Processed", value="100M+", delta="Rows")
    with col3:
        st.metric(label="Automation Efficiency", value="40%", delta="Saved Time")

# --- PAGE 2: CORE PROJECTS ---
elif page == "Core Projects":
    st.title("Featured Projects 🚀")
    st.write("Browse through an assortment of my recent professional applications.")
    
    # Project 1 Container Card
    with st.container(border=True):
        st.markdown("### 📊 Cloud-Native E-Commerce Analytics Tool")
        st.caption("🛠️ Tech Stack: `Python` | `Streamlit` | `Pandas` | `Plotly`")
        st.write("""
        Engineered an enterprise-level dashboard monitoring retail store transactions. 
        Integrated dynamic clustering logic to automatically segment purchasing personas, increasing retention rates by 18%.
        """)
        st.link_button("📂 View Git Repository", "https://github.com")

    st.write("") # Spacing

    # Project 2 Container Card
    with st.container(border=True):
        st.markdown("### 🤖 Automated Pipeline Scheduling Engine")
        st.caption("🛠️ Tech Stack: `Python` | `SQL` | `Docker` | `AWS Lambda`")
        st.write("""
        Built an automated database validation worker that runs micro-audits across thousands of data points daily, 
        reducing database formatting errors down to absolute zero.
        """)
        st.link_button("📁 Read Technical Documentation", "https://github.com")

# --- PAGE 3: TECHNICAL SKILLS ---
elif page == "Technical Skills":
    st.title("Technical Proficiency 🛠️")
    st.write("A comprehensive breakdown of tools, programming languages, and engineering concepts I use daily.")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💻 Core Programming")
        st.success("**Python** (Advanced Data Engineering)")
        st.success("**SQL** (Complex Joins & Optimization)")
        st.success("**HTML & CSS** (Responsive UI Styling)")
    
    with col2:
        st.markdown("### ⚙️ Frameworks & Infrastructure")
        st.success("**Streamlit** (Rapid App Development)")
        st.success("**Pandas & NumPy** (Statistical Calculations)")
        st.success("**Git & GitHub** (Version Control Strategy)")

    st.divider()
    st.markdown("### 🌟 Areas of Focus")
    st.write("- **Data Architecture:** Designing scalable database management layouts.")
    st.write("- **Workflow Automation:** Replacing manual data pipelines with automated scripts.")

# --- PAGE 4: CONTACT & LINKS ---
elif page == "Contact & Links":
    st.title("Establish Connection 📧")
    st.write("I am always interested in discussing new freelance agreements, corporate positions, or automation consulting.")
    
    st.divider()
    
    # Clean professional contact channels
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 👔 Professional Networks")
        st.link_button("💼 Connect on LinkedIn", "https://www.linkedin.com/in/jharold-legaspi/")
    with col2:
        st.markdown("#### 🐙 Code Repositories")
        st.link_button("💻 Explore My GitHub", "https://github.com/cutepotato24")
    with col3:
        st.markdown("#### 📧 Direct Contact")
        st.link_button("� Send an Email", "jllegaspicareers@gmail.com")
        
    st.write("")
    st.write("")
    st.write("")
    st.success("📩 **Direct Contact:** Please feel free to open a conversation or drop professional references through my social channels.")
