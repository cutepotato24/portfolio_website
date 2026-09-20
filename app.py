import streamlit as st

# 1. Page Configuration (Must be the first command)
st.set_page_config(
    page_title="Professional Portfolio",
    page_icon="🔷",
    layout="centered",
)

# Pure charcoal, white, and electric-blue theme.
st.markdown(
    """
    <style>
        :root {
            --charcoal: #17191c;
            --charcoal-soft: #22262b;
            --white: #f5f7fa;
            --muted: #aeb6c2;
            --blue: #39a8ff;
            --blue-dark: #0d2638;
            --border: #3a414a;
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
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p {
            color: var(--white);
        }

        [data-testid="stSidebar"] [role="radiogroup"] label {
            color: var(--muted);
        }

        [data-testid="stSidebar"] [role="radiogroup"] label:hover {
            color: var(--blue);
        }

        .main .block-container {
            max-width: 1000px;
            padding: 3rem 2.5rem 5rem;
        }

        h1, h2, h3, h4 {
            color: var(--white) !important;
        }

        .icon {
            color: var(--blue);
        }

        h1 {
            letter-spacing: -0.03em;
        }

        p, li {
            color: var(--muted);
            line-height: 1.7;
        }

        a {
            color: var(--blue) !important;
        }

        code {
            background: var(--blue-dark) !important;
            border: 1px solid #194766;
            color: var(--blue) !important;
        }

        [data-testid="stMetric"] {
            background: var(--charcoal-soft);
            border: 1px solid var(--border);
            border-top: 2px solid var(--blue);
            padding: 1rem;
        }

        [data-testid="stMetricLabel"],
        [data-testid="stMetricDelta"] {
            color: var(--muted) !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--white) !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--charcoal-soft);
            border: 1px solid var(--border);
            border-left: 3px solid var(--blue);
            border-radius: 3px;
            padding: 0.75rem 1rem;
        }

        [data-testid="stLinkButton"] {
            background: var(--blue) !important;
            border: 0 !important;
            border-radius: 3px !important;
            color: #07131d !important;
            font-weight: 700 !important;
        }

        [data-testid="stLinkButton"]:hover {
            background: var(--white) !important;
            color: #07131d !important;
        }

        [data-testid="stAlert"] {
            background: var(--blue-dark) !important;
            border: 1px solid #194766 !important;
            color: var(--white) !important;
        }

        hr {
            border-color: var(--border) !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 2. Sidebar Structural Navigation
st.sidebar.markdown("## <span class='icon'>☰︎</span> Navigation", unsafe_allow_html=True)
page = st.sidebar.radio("Go to:", ["Profile Overview", "Core Projects", "Technical Skills", "Contact & Links"])

# --- PAGE 1: PROFILE OVERVIEW ---
if page == "Profile Overview":
    st.title("Hi, Thanks for visiting! ✦︎")
    st.subheader("I'm Harold, Analytics & vibe Software Engineer")

    st.info("⚡︎ I specialized in building automated data workflows and clean user experiences for data and business intelligence applications.")

    st.markdown("### <span class='icon'>◎︎</span> Professional Profile", unsafe_allow_html=True)
    st.write("""
    I am a results-driven data professional dedicated to transforming complex data sets into clear, actionable business strategies.
    By leveraging cloud-native workflows, I design and implement reliable pipeline structures that help organizations scale.
    """)
    st.markdown(
        '<a href="https://drive.google.com/uc?export=download&id=1XKYToQWmjtwlD5xTLvT9n21h9b0xeWY7" '
        'style="text-decoration: underline;">⇩ Download My Updated Resume</a>',
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown("### <span class='icon'>▣︎</span> Career Statistics", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Python Projects", value="12+", delta="Active")
    with col2:
        st.metric(label="Data Processed", value="100M+", delta="Rows")
    with col3:
        st.metric(label="Automation Efficiency", value="40%", delta="Saved Time")

# --- PAGE 2: CORE PROJECTS ---
elif page == "Core Projects":
    st.title("Featured Projects ◈︎")
    st.write("Browse through an assortment of my recent professional applications.")

    with st.container(border=True):
        st.markdown("### <span class='icon'>◈︎</span> Cloud-Native E-Commerce Analytics Tool", unsafe_allow_html=True)
        st.caption("⚙︎ Tech Stack: `Python` | `Streamlit` | `Pandas` | `Plotly`")
        st.write("""
        Engineered an enterprise-level dashboard monitoring retail store transactions.
        Integrated dynamic clustering logic to automatically segment purchasing personas, increasing retention rates by 18%.
        """)
        st.link_button("↗︎ View Git Repository", "https://github.com")

    st.write("")

    with st.container(border=True):
        st.markdown("### <span class='icon'>◈︎</span> Automated Pipeline Scheduling Engine", unsafe_allow_html=True)
        st.caption("⚙︎ Tech Stack: `Python` | `SQL` | `Docker` | `AWS Lambda`")
        st.write("""
        Built an automated database validation worker that runs micro-audits across thousands of data points daily,
        reducing database formatting errors down to absolute zero.
        """)
        st.link_button("↗︎ Read Technical Documentation", "https://github.com")

    st.write("")

    with st.container(border=True):
        st.markdown("### <span class='icon'>◈︎</span> Maven Analytics Hospital rating Viz Challenge", unsafe_allow_html=True)
        st.caption("⚙︎ Tools: `Microsoft Excel` | `Tableau` | `Data Visualization` | `Dashboard Design`")
        st.write("""
        Created a data visualization project using Excel for data preparation and analysis, then Tableau to transform
        the results into an interactive dashboard. This project demonstrates my ability to organize data, identify
        meaningful trends, and communicate insights through clear and engaging visualizations.
        """)
        link_col1, link_col2 = st.columns(2, gap="small")
        with link_col1:
            st.link_button(
                "↗︎ Maven Viz",
                "https://public.tableau.com/app/profile/john.harold.legaspi6572/viz/MAVENMODELEDDATATableau/Dashboard1#1",
            )
        with link_col2:
            st.link_button(
                "↗︎ Onyx Viz",
                "https://public.tableau.com/app/profile/john.harold.legaspi6572/viz/OnyxDataaugust2023DNAChallenge/Dashboard1",
            )

# --- PAGE 3: TECHNICAL SKILLS ---
elif page == "Technical Skills":
    st.title("Technical Proficiency ⌘︎")
    st.write("A comprehensive breakdown of tools, programming languages, and engineering concepts I use daily.")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### <span class='icon'>⌘︎</span> Core Programming", unsafe_allow_html=True)
        st.success("**Python** (Advanced Data Engineering)")
        st.success("**SQL** (Complex Joins & Optimization)")
        st.success("**HTML & CSS** (Responsive UI Styling)")

    with col2:
        st.markdown("### <span class='icon'>⚙︎</span> Frameworks & Infrastructure", unsafe_allow_html=True)
        st.success("**Streamlit** (Rapid App Development)")
        st.success("**Pandas & NumPy** (Statistical Calculations)")
        st.success("**Git & GitHub** (Version Control Strategy)")

    st.divider()
    st.markdown("### <span class='icon'>✦︎</span> Areas of Focus", unsafe_allow_html=True)
    st.write("- **Data Architecture:** Designing scalable database management layouts.")
    st.write("- **Workflow Automation:** Replacing manual data pipelines with automated scripts.")

# --- PAGE 4: CONTACT & LINKS ---
elif page == "Contact & Links":
    st.title("Establish Connection ✉︎")
    st.write("I am always interested in discussing new freelance agreements, corporate positions, or automation consulting.")

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### <span class='icon'>♙︎</span> Professional Networks", unsafe_allow_html=True)
        st.link_button("↗︎ Connect on LinkedIn", "https://www.linkedin.com/in/jharold-legaspi/")
    with col2:
        st.markdown("#### <span class='icon'>⌘︎</span> Code Repositories", unsafe_allow_html=True)
        st.link_button("↗︎ Explore My GitHub", "https://github.com/cutepotato24")
    with col3:
        st.markdown("#### <span class='icon'>✉︎</span> Direct Email Contact", unsafe_allow_html=True)
        st.link_button("↗︎ Email Me", "https://mail.google.com/mail/?view=cm&fs=1&to=jllegaspicareers@gmail.com")

    st.write("")
    st.success("✉︎ **Direct Contact:** Please feel free to open a conversation or drop professional references through my social channels.")
