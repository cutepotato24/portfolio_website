import streamlit as st
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Professional Portfolio",
    page_icon="💼",
    layout="centered"
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Profile Overview"


# ============================================================
# CHROME-STYLE CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       PAGE
       ======================================================== */

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       CHROME TAB BAR
       ======================================================== */

    .chrome-tabs-container {
        width: 100%;
        background: #dee1e6;
        border-bottom: 1px solid #b8bcc2;

        display: flex;
        align-items: flex-end;

        padding: 8px 8px 0 8px;

        box-sizing: border-box;

        overflow-x: auto;

        margin-bottom: 30px;
    }


    /* Remove scrollbar */

    .chrome-tabs-container::-webkit-scrollbar {
        height: 0;
    }


    /* ========================================================
       INDIVIDUAL TAB
       ======================================================== */

    .chrome-tab-link {

        position: relative;

        display: flex;
        align-items: center;
        justify-content: center;

        min-width: 170px;
        height: 40px;

        padding: 0 22px;

        margin-right: 2px;

        background: #cfd2d6;

        color: #3c4043;

        text-decoration: none !important;

        font-family: Arial, sans-serif;

        font-size: 14px;

        font-weight: 500;

        border: 1px solid #b8bcc2;

        border-bottom: none;

        border-radius: 9px 9px 0 0;

        transition:
            background 0.15s ease,
            color 0.15s ease;

        white-space: nowrap;

        box-sizing: border-box;
    }


    /* ========================================================
       TAB HOVER
       ======================================================== */

    .chrome-tab-link:hover {

        background: #e3e5e8;

        color: #202124;

        text-decoration: none !important;
    }


    /* ========================================================
       ACTIVE TAB
       ======================================================== */

    .chrome-tab-link.active {

        background: #ffffff;

        color: #202124;

        border-color: #b8bcc2;

        border-bottom: 1px solid #ffffff;

        margin-bottom: -1px;

        z-index: 2;

        font-weight: 600;
    }


    /* ========================================================
       ACTIVE TAB HOVER
       ======================================================== */

    .chrome-tab-link.active:hover {

        background: #ffffff;

        color: #202124;
    }


    /* ========================================================
       CONTENT AREA
       ======================================================== */

    .content-area {

        background: #ffffff;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 700px) {

        .chrome-tabs-container {

            padding-left: 4px;
            padding-right: 4px;
        }


        .chrome-tab-link {

            min-width: 130px;

            height: 38px;

            padding: 0 14px;

            font-size: 12px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE NAVIGATION
# ============================================================

pages = [
    "Profile Overview",
    "Core Projects",
    "Technical Skills",
    "Contact & Links"
]


# ============================================================
# READ PAGE FROM URL
# ============================================================

if "page" in st.query_params:

    requested_page = st.query_params["page"]

    if requested_page in pages:

        st.session_state.page = requested_page


# ============================================================
# CHROME TAB NAVIGATION
# ============================================================

tabs_html = '<div class="chrome-tabs-container">'

for page in pages:

    active_class = (
        "active"
        if st.session_state.page == page
        else ""
    )

    tabs_html += f"""
        <a
            class="chrome-tab-link {active_class}"
            href="?page={page}"
        >
            {page}
        </a>
    """


tabs_html += "</div>"


st.markdown(
    tabs_html,
    unsafe_allow_html=True
)


# ============================================================
# PROFILE OVERVIEW
# ============================================================

if st.session_state.page == "Profile Overview":

    st.title("Hi, I'm Harold, how are you today? 👋")


    profile_image = Path("assets/profile.png")


    left_col, right_col = st.columns([1, 2])


    # --------------------------------------------------------
    # PROFILE IMAGE
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    with right_col:

        st.subheader("Analytics & Software Engineer")

        st.write(
            """
            Passionate about data engineering, automation,
            analytics, and building practical software solutions.
            """
        )


    # --------------------------------------------------------
    # HIGHLIGHT
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
# CORE PROJECTS
# ============================================================

elif st.session_state.page == "Core Projects":

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
            and improve data quality across automated workflows.
            """
        )


        st.link_button(
            "📁 Read Technical Documentation",
            "https://github.com"
        )


# ============================================================
# TECHNICAL SKILLS
# ============================================================

elif st.session_state.page == "Technical Skills":

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
    # FRAMEWORKS
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
# CONTACT & LINKS
# ============================================================

elif st.session_state.page == "Contact & Links":

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
    # LINKEDIN
    # --------------------------------------------------------

    with col1:

        st.markdown("#### 👔 Professional Networks")


        st.link_button(
            "💼 Connect on LinkedIn",
            "https://linkedin.com"
        )


    # --------------------------------------------------------
    # GITHUB
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
    # CONTACT
    # --------------------------------------------------------

    st.success(
        "📩 **Direct Contact:** Please feel free to open "
        "a conversation or drop professional references "
        "through my social channels."
    )