import streamlit as st
from pathlib import Path


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Professional Portfolio",
    page_icon="💼",
    layout="centered"
)


# ============================================================
# 2. CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GENERAL PAGE
       ======================================================== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       TAB BAR
       ======================================================== */

    div[data-baseweb="tab-list"] {
        display: flex !important;

        gap: 10px !important;

        padding: 10px 5px !important;

        border: none !important;

        background: transparent !important;

        justify-content: center !important;
    }


    /* ========================================================
       INDIVIDUAL TABS
       ======================================================== */

    div[data-baseweb="tab-list"] > button {
        background-color: #d3d3d3 !important;

        color: #333333 !important;

        border: 2px solid #a9a9a9 !important;

        border-radius: 12px !important;

        padding: 10px 18px !important;

        margin: 0 !important;

        min-height: 45px !important;

        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08) !important;

        transition:
            background-color 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease,
            transform 0.2s ease !important;
    }


    /* ========================================================
       TAB TEXT
       ======================================================== */

    div[data-baseweb="tab-list"] > button div {
        color: #333333 !important;

        font-weight: 500 !important;
    }


    /* ========================================================
       TAB HOVER
       ======================================================== */

    div[data-baseweb="tab-list"] > button:hover {
        background-color: #bdbdbd !important;

        border-color: #8f8f8f !important;

        box-shadow: 0 3px 7px rgba(0, 0, 0, 0.15) !important;

        transform: translateY(-1px);
    }


    /* ========================================================
       ACTIVE TAB
       ======================================================== */

    div[data-baseweb="tab-list"]
    > button[aria-selected="true"] {

        background-color: #707070 !important;

        color: white !important;

        border: 2px solid #5c5c5c !important;

        border-radius: 12px !important;

        font-weight: 700 !important;

        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.20) !important;
    }


    /* ========================================================
       ACTIVE TAB TEXT
       ======================================================== */

    div[data-baseweb="tab-list"]
    > button[aria-selected="true"] div {

        color: white !important;

        font-weight: 700 !important;
    }


    /* ========================================================
       REMOVE STREAMLIT DEFAULT TAB UNDERLINE
       ======================================================== */

    div[data-baseweb="tab-highlight"] {
        display: none !important;
    }


    /* ========================================================
       REMOVE DEFAULT TAB BORDER
       ======================================================== */

    div[data-baseweb="tab-border"] {
        display: none !important;
    }


    /* ========================================================
       LINK BUTTONS
       ======================================================== */

    div[data-testid="stLinkButton"] a {
        border-radius: 8px !important;
    }


    /* ========================================================
       MOBILE RESPONSIVE DESIGN
       ======================================================== */

    @media (max-width: 700px) {

        div[data-baseweb="tab-list"] {

            gap: 6px !important;

            justify-content: flex-start !important;

            overflow-x: auto !important;

            padding: 8px 3px !important;
        }


        div[data-baseweb="tab-list"] > button {

            padding: 8px 12px !important;

            min-height: 40px !important;

            white-space: nowrap !important;

            border-radius: 10px !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 3. TAB NAVIGATION
# ============================================================

profile_tab, projects_tab, skills_tab, contact_tab = st.tabs(
    [
        "Profile Overview",
        "Core Projects",
        "Technical Skills",
        "Contact & Links"
    ]
)


# ============================================================
# PAGE 1 — PROFILE OVERVIEW
# ============================================================

with profile_tab:

    st.title("Hi, I'm Harold, how are you today? 👋")


    # --------------------------------------------------------
    # PROFILE SECTION
    # --------------------------------------------------------

    profile_image = Path("assets/profile.png")

    left_col, right_col = st.columns([1, 2])


    with left_col:

        if profile_image.exists():

            st.image(
                str(profile_image),
                width=220,
                caption="Harold"
            )

        else:

            st.warning(
                "Add your photo to "
                "`assets/profile.png` to show it here."
            )


    with right_col:

        st.subheader("Analytics & Software Engineer")

        st.write(
            """
            Passionate about data engineering, automation,
            analytics, and building practical software solutions.
            """
        )


    # --------------------------------------------------------
    # HIGHLIGHT BANNER
    # --------------------------------------------------------

    st.info(
        "🚀 Specialized in building automated data workflows "
        "and clean user experiences."
    )


    # --------------------------------------------------------
    # PROFESSIONAL PROFILE
    # --------------------------------------------------------

    st.markdown("### 🎯 Professional Profile")

    st.write(
        """
        I am a results-driven professional dedicated to
        transforming complex data sets into clear, actionable
        business strategies.

        By leveraging cloud-native Python workflows, I design
        and implement reliable pipeline structures that help
        organizations scale.
        """
    )


    st.divider()


    # --------------------------------------------------------
    # CAREER STATISTICS
    # --------------------------------------------------------

    st.markdown("### 📊 Career Statistics")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            label="Python Projects",
            value="12+",
            delta="Active"
        )


    with col2:

        st.metric(
            label="Data Processed",
            value="100M+",
            delta="Rows"
        )


    with col3:

        st.metric(
            label="Automation Efficiency",
            value="40%",
            delta="Saved Time"
        )


# ============================================================
# PAGE 2 — CORE PROJECTS
# ============================================================

with projects_tab:

    st.title("Featured Projects 🚀")

    st.write(
        "Browse through an assortment of my recent "
        "professional applications."
    )


    # --------------------------------------------------------
    # PROJECT 1
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown(
            "### 📊 Cloud-Native E-Commerce Analytics Tool"
        )

        st.caption(
            "🛠️ Tech Stack: "
            "`Python` | `Streamlit` | `Pandas` | `Plotly`"
        )

        st.write(
            """
            Engineered an enterprise-level dashboard monitoring
            retail store transactions.

            Integrated dynamic clustering logic to automatically
            segment purchasing personas, increasing retention
            rates by 18%.
            """
        )

        st.link_button(
            "📂 View Git Repository",
            "https://github.com"
        )


    st.write("")


    # --------------------------------------------------------
    # PROJECT 2
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown(
            "### 🤖 Automated Pipeline Scheduling Engine"
        )

        st.caption(
            "🛠️ Tech Stack: "
            "`Python` | `SQL` | `Docker` | `AWS Lambda`"
        )

        st.write(
            """
            Built an automated database validation worker that
            runs micro-audits across thousands of data points
            daily.

            The system helps reduce database formatting errors
            and improves data quality across automated workflows.
            """
        )

        st.link_button(
            "📁 Read Technical Documentation",
            "https://github.com"
        )


# ============================================================
# PAGE 3 — TECHNICAL SKILLS
# ============================================================

with skills_tab:

    st.title("Technical Proficiency 🛠️")

    st.write(
        """
        A comprehensive breakdown of tools, programming
        languages, and engineering concepts I use daily.
        """
    )


    st.divider()


    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # CORE PROGRAMMING
    # --------------------------------------------------------

    with col1:

        st.markdown("### 💻 Core Programming")

        st.success(
            "**Python** (Advanced Data Engineering)"
        )

        st.success(
            "**SQL** (Complex Joins & Optimization)"
        )

        st.success(
            "**HTML & CSS** (Responsive UI Styling)"
        )


    # --------------------------------------------------------
    # FRAMEWORKS & INFRASTRUCTURE
    # --------------------------------------------------------

    with col2:

        st.markdown("### ⚙️ Frameworks & Infrastructure")

        st.success(
            "**Streamlit** (Rapid App Development)"
        )

        st.success(
            "**Pandas & NumPy** (Statistical Calculations)"
        )

        st.success(
            "**Git & GitHub** (Version Control Strategy)"
        )


    st.divider()


    # --------------------------------------------------------
    # AREAS OF FOCUS
    # --------------------------------------------------------

    st.markdown("### 🌟 Areas of Focus")

    st.write(
        "- **Data Architecture:** Designing scalable "
        "database management layouts."
    )

    st.write(
        "- **Workflow Automation:** Replacing manual data "
        "pipelines with automated scripts."
    )


# ============================================================
# PAGE 4 — CONTACT & LINKS
# ============================================================

with contact_tab:

    st.title("Establish Connection 📧")

    st.write(
        """
        I am always interested in discussing new freelance
        agreements, corporate positions, or automation consulting.
        """
    )


    st.divider()


    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # PROFESSIONAL NETWORKS
    # --------------------------------------------------------

    with col1:

        st.markdown("#### 👔 Professional Networks")

        st.link_button(
            "💼 Connect on LinkedIn",
            "https://linkedin.com"
        )


    # --------------------------------------------------------
    # CODE REPOSITORIES
    # --------------------------------------------------------

    with col2:

        st.markdown("#### 🐙 Code Repositories")

        st.link_button(
            "💻 Explore My GitHub",
            "https://github.com"
        )


    st.write("")
    st.write("")


    # --------------------------------------------------------
    # DIRECT CONTACT
    # --------------------------------------------------------

    st.success(
        "📩 **Direct Contact:** Please feel free to open "
        "a conversation or drop professional references "
        "through my social channels."
    )