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

    .chrome-tab-bar {
        display: flex;

        align-items: flex-end;

        width: 100%;

        height: 52px;

        background: #e8eaed;

        border-bottom: 1px solid #c4c7c5;

        padding-left: 8px;

        margin-bottom: 25px;

        overflow-x: auto;
    }


    /* ========================================================
       TAB WRAPPER
       ======================================================== */

    .chrome-tab {
        position: relative;

        margin-right: 2px;

        min-width: 150px;

        height: 43px;
    }


    /* ========================================================
       NORMAL TAB
       ======================================================== */

    .chrome-tab button {

        position: absolute;

        left: 0;
        right: 0;
        bottom: 0;

        width: 100% !important;

        height: 43px !important;

        padding: 0 18px !important;

        background: #d5d8dc !important;

        color: #4a4d50 !important;

        border: 1px solid #c0c3c6 !important;

        border-bottom: none !important;

        border-radius: 10px 10px 0 0 !important;

        box-shadow: none !important;

        font-size: 14px !important;

        font-weight: 500 !important;

        white-space: nowrap !important;

        transition:
            background 0.15s ease,
            color 0.15s ease !important;
    }


    /* ========================================================
       NORMAL TAB HOVER
       ======================================================== */

    .chrome-tab button:hover {

        background: #e1e3e6 !important;

        color: #202124 !important;

        border-color: #b5b8bb !important;
    }


    /* ========================================================
       ACTIVE CHROME TAB
       ======================================================== */

    .chrome-active button {

        position: absolute;

        left: 0;
        right: 0;
        bottom: 0;

        width: 100% !important;

        height: 45px !important;

        padding: 0 18px !important;

        background: #ffffff !important;

        color: #202124 !important;

        border: 1px solid #c4c7c5 !important;

        border-bottom: 1px solid #ffffff !important;

        border-radius: 10px 10px 0 0 !important;

        box-shadow: none !important;

        font-size: 14px !important;

        font-weight: 600 !important;

        white-space: nowrap !important;

        z-index: 5 !important;
    }


    /* ========================================================
       ACTIVE TAB HOVER
       ======================================================== */

    .chrome-active button:hover {

        background: #ffffff !important;

        color: #202124 !important;
    }


    /* ========================================================
       REMOVE STREAMLIT BUTTON EXTRA SPACING
       ======================================================== */

    .chrome-tab div[data-testid="stButton"],
    .chrome-active div[data-testid="stButton"] {

        margin: 0 !important;

        padding: 0 !important;
    }


    /* ========================================================
       CONTENT AREA
       ======================================================== */

    .content-area {

        background: #ffffff;

        border-radius: 0 0 10px 10px;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 700px) {

        .chrome-tab-bar {

            height: 50px;

            justify-content: flex-start;

            overflow-x: auto;

            padding-left: 5px;
        }

        .chrome-tab {

            min-width: 130px;

            height: 41px;
        }

        .chrome-tab button,
        .chrome-active button {

            height: 41px !important;

            font-size: 12px !important;

            padding: 0 12px !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# NAVIGATION FUNCTION
# ============================================================

def chrome_tab(label):

    is_active = st.session_state.page == label

    if is_active:

        st.markdown(
            '<div class="chrome-tab chrome-active">',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="chrome-tab">',
            unsafe_allow_html=True
        )

    clicked = st.button(
        label,
        key=f"chrome_{label}",
        use_container_width=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    if clicked:

        st.session_state.page = label

        st.rerun()


# ============================================================
# CHROME TAB NAVIGATION
# ============================================================

st.markdown(
    '<div class="chrome-tab-bar">',
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4 = st.columns(
    [1, 1, 1, 1],
    gap="small"
)


with tab1:
    chrome_tab("Profile Overview")


with tab2:
    chrome_tab("Core Projects")


with tab3:
    chrome_tab("Technical Skills")


with tab4:
    chrome_tab("Contact & Links")


st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# ============================================================
# PROFILE OVERVIEW
# ============================================================

if st.session_state.page == "Profile Overview":

    st.title("Hi, I'm Harold, how are you today? 👋")

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


    st.info(
        "🚀 Specialized in building automated data workflows "
        "and clean user experiences."
    )


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


    with col1:

        st.markdown("#### 👔 Professional Networks")

        st.link_button(
            "💼 Connect on LinkedIn",
            "https://linkedin.com"
        )


    with col2:

        st.markdown("#### 🐙 Code Repositories")

        st.link_button(
            "💻 Explore My GitHub",
            "https://github.com"
        )


    st.write("")
    st.write("")

    st.success(
        "📩 **Direct Contact:** Please feel free to open "
        "a conversation or drop professional references "
        "through my social channels."
    )


