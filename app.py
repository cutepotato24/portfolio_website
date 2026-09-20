import streamlit as st

st.set_page_config(
    page_title="Harold | Analytics and Software Engineer",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        :root {
            --charcoal: #17191c;
            --charcoal-soft: #202328;
            --white: #f5f7fa;
            --muted: #aeb6c2;
            --blue: #39a8ff;
            --blue-dark: #0d2638;
            --border: #353b44;
        }

        .stApp {
            background: var(--charcoal);
            color: var(--white);
        }

        [data-testid="stSidebar"] {
            background: #111315;
            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p {
            color: var(--white);
        }

        [data-testid="stSidebar"] .stRadio > label {
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        [data-testid="stSidebar"] [role="radiogroup"] label {
            color: var(--muted);
        }

        [data-testid="stSidebar"] [role="radiogroup"] label:hover,
        [data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {
            color: var(--blue);
        }

        .main .block-container {
            max-width: 980px;
            padding: 5rem 3rem 6rem;
        }

        h1, h2, h3 {
            color: var(--white) !important;
            letter-spacing: -0.02em;
        }

        h1 {
            font-size: clamp(2.5rem, 6vw, 5rem) !important;
            line-height: 1 !important;
            margin-bottom: 0.5rem !important;
        }

        h2 {
            border-bottom: 1px solid var(--border);
            font-size: 1.35rem !important;
            margin-top: 2.75rem !important;
            padding-bottom: 0.7rem;
        }

        h3 {
            font-size: 1.05rem !important;
            margin-top: 1.5rem !important;
        }

        p, li {
            color: var(--muted);
            line-height: 1.7;
        }

        a {
            color: var(--blue) !important;
            font-weight: 600;
        }

        code {
            background: var(--blue-dark) !important;
            border: 1px solid #194766;
            color: var(--blue) !important;
        }

        .eyebrow {
            color: var(--blue);
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            margin-bottom: 1rem;
            text-transform: uppercase;
        }

        .subtitle {
            color: var(--muted);
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        .project {
            border-left: 2px solid var(--blue);
            margin: 1.75rem 0;
            padding: 0.25rem 0 0.25rem 1.25rem;
        }

        .project p {
            margin-bottom: 0.5rem;
        }

        .contact-line {
            border-bottom: 1px solid var(--border);
            padding: 1rem 0;
        }

        .contact-label {
            color: var(--muted);
            display: inline-block;
            min-width: 6rem;
        }

        .stButton > button, [data-testid="stLinkButton"] {
            background: var(--blue) !important;
            border: 0 !important;
            border-radius: 3px !important;
            color: #07131d !important;
            font-weight: 700 !important;
        }

        .stButton > button:hover, [data-testid="stLinkButton"]:hover {
            background: var(--white) !important;
            color: #07131d !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("HAROLD")
page = st.sidebar.radio(
    "Sections",
    ["Overview", "Projects", "Skills", "Contact"],
)

if page == "Overview":
    st.markdown('<div class="eyebrow">Analytics / Software Engineering</div>', unsafe_allow_html=True)
    st.title("Harold")
    st.markdown('<div class="subtitle">Precise systems. Useful data. Clear outcomes.</div>', unsafe_allow_html=True)
    st.write(
        "I build automated data workflows and software that turn complex information "
        "into clear, useful business decisions."
    )

    st.header("Profile")
    st.write(
        "I design reliable Python pipelines, data tools, and focused user experiences "
        "for organizations that need to work with data at scale."
    )

    st.header("Selected figures")
    col1, col2, col3 = st.columns(3)
    col1.metric("Python projects", "12+")
    col2.metric("Data processed", "100M+")
    col3.metric("Efficiency saved", "40%")

elif page == "Projects":
    st.markdown('<div class="eyebrow">Selected work</div>', unsafe_allow_html=True)
    st.title("Projects")

    st.markdown('<div class="project">', unsafe_allow_html=True)
    st.subheader("Cloud-Native E-Commerce Analytics Tool")
    st.caption("Python / Streamlit / Pandas / Plotly")
    st.write("A dashboard for monitoring retail transactions and segmenting purchasing behavior.")
    st.markdown("[View Git Repository](https://github.com)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="project">', unsafe_allow_html=True)
    st.subheader("Automated Pipeline Scheduling Engine")
    st.caption("Python / SQL / Docker / AWS Lambda")
    st.write("An automated database validation worker that checks thousands of data points each day.")
    st.markdown("[Read Technical Documentation](https://github.com)")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Skills":
    st.markdown('<div class="eyebrow">Technical toolkit</div>', unsafe_allow_html=True)
    st.title("Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Programming")
        st.write("Python")
        st.write("SQL")
        st.write("HTML and CSS")
    with col2:
        st.header("Infrastructure")
        st.write("Streamlit")
        st.write("Pandas and NumPy")
        st.write("Git and GitHub")

    st.header("Focus areas")
    st.write("Data architecture")
    st.write("Workflow automation")
    st.write("Pipeline reliability")

elif page == "Contact":
    st.markdown('<div class="eyebrow">Start a conversation</div>', unsafe_allow_html=True)
    st.title("Contact")
    st.write("Available for freelance work, engineering roles, and consulting.")

    st.markdown(
        '<div class="contact-line"><span class="contact-label">LinkedIn</span>'
        '<a href="https://www.linkedin.com/in/jharold-legaspi/">jharold-legaspi</a></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="contact-line"><span class="contact-label">GitHub</span>'
        '<a href="https://github.com/cutepotato24">cutepotato24</a></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="contact-line"><span class="contact-label">Email</span>'
        '<a href="https://mail.google.com/mail/?view=cm&fs=1&to=jllegaspicareers@gmail.com">'
        'jllegaspicareers@gmail.com</a></div>',
        unsafe_allow_html=True,
    )
