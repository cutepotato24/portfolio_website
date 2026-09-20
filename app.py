import streamlit as st
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Professional Portfolio",
    page_icon="💼",
    layout="centered",
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Profile Overview"


# ============================================================
# CHROME-STYLE TAB CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GENERAL PAGE
       ======================================================== */

    .block-container {
        max-width: 1150px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       CHROME TAB STRIP
       ======================================================== */

    .chrome-tabs {
        background: #bfc1c4;
        border-bottom: 1px solid #8f9296;

        padding: 8px 8px 0 8px;
        margin-bottom: 30px;

        border-radius: 12px 12px 0 0;
        overflow-x: auto;
    }


    /* Only affect columns inside the tab bar */
    .chrome-tabs [data-testid="stHorizontalBlock"] {
        gap: 4px !important;
        align-items: flex-end !important;
    }


    .chrome-tabs [data-testid="column"] {
        padding: 0 !important;
        min-width: 0 !important;
    }


    /* ========================================================
       TAB BUTTON CONTAINERS
       ======================================================== */

    .chrome-tabs [data-testid="stButton"] {
        margin: 0 !important;
        padding: 0 !important;
    }


    /* ========================================================
       INACTIVE TABS
       ======================================================== */

    .chrome-tabs button {
        width: 100% !important;

        height: 42px !important;
        min-height: 42px !important;

        padding: 0 16px !important;

        background: #d2d4d7 !important;
        color: #3c4043 !important;

        border: 1px solid #aeb1b5 !important;
        border-bottom: none !important;

        border-radius: 11px 11px 0 0 !important;

        box-shadow:
            0 -1px 0 rgba(255, 255, 255, 0.35) inset,
            0 1px 2px rgba(0, 0, 0, 0.08) !important;

        font-size: 14px !important;
        font-weight: 500 !important;

        white-space: nowrap !important;

        transition:
            background 0.15s ease,
            color 0.15s ease,
            transform 0.15s ease !important;
    }


    /* ========================================================
       TAB HOVER
       ======================================================== */

    .chrome-tabs button:hover {
        background: #e7e8ea !important;
        color: #202124 !important;

        border-color: #999da2 !important;

        transform: translateY(-1px);
    }


    /* ========================================================
       TAB FOCUS
       ======================================================== */

    .chrome-tabs button:focus,
    .chrome-tabs button:focus-visible {
        outline: none !important;

        box-shadow:
            0 -1px 0 rgba(255, 255, 255, 0.35) inset,
            0 1px 2px rgba(0, 0, 0, 0.08) !important;
    }


    /* ========================================================
       ACTIVE TAB
       ======================================================== */

    .chrome-tabs .active-tab button {
        position: relative;
        z-index: 3;

        background: #ffffff !important;
        color: #202124 !important;

        border-color: #aeb1b5 !important;
        border-bottom: 1px solid #ffffff !important;

        font-weight: 600 !important;

        box-shadow: none !important;
    }


    .chrome-tabs .active-tab button:hover {
        background: #ffffff !important;
        color: #202124 !important;

        transform: none !important;
    }


    /* ========================================================
       PAGE CONTENT
       ======================================================== */

    .portfolio-content {
        background: #ffffff;
    }


    /* ========================================================
       MOBILE RESPONSIVENESS
       ======================================================== */

    @media (max-width: 700px) {

        .chrome-tabs {
            padding: 6px 5px 0 5px;
        }

        .chrome-tabs [data-testid="stHorizontalBlock"] {
            gap: 2px !important;
        }

        .chrome-tabs button {
            height: 38px !important;
            min-height: 38px !important;

            padding: 0 8px !important;

            font-size: 11px !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# NAVIGATION FUNCTION
# ============================================================

def tab_button(label):
    is_active = st.session_state.page == label

    if is_active:
        st.markdown(
            '<div class="active-tab">',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="inactive-tab">',
            unsafe_allow_html=True,
        )

    clicked = st.button(
        label,
        key=f"tab_{label}",
        use_container_width=True,
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    if clicked and st.session_state.page != label:
        st.session_state.page = label
        st.rerun()


# ============================================================
# CHROME TAB BAR
# ============================================================

st.markdown(
    '<div class="chrome-tabs">',
    unsafe_allow_html=True,
)

tab1, tab2, tab3, tab4 = st.columns(
    [1.2, 1, 1, 1],
    gap="small",
)

with tab1:
    tab_button("Profile Overview")

with tab2:
    tab_button("Core Projects")

with tab3:
    tab_button("Technical Skills")

with tab4:
    tab_button("Contact & Links")

st.markdown(
    "</div>",
    unsafe_allow_html=True,
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
                caption="Harold",
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
            delta="Active",
        )

    with col2:
        st.metric(
            label="Data Processed",
            value="100M+",
            delta="Rows",
        )

    with col3:
        st.metric(
            label="Automation Efficiency",
            value="40%",
            delta="Saved Time",
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
            "https://github.com",
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
            "https://github.com",
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
    # PROGRAMMING
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
            "https://linkedin.com",
        )

    # --------------------------------------------------------
    # GITHUB
    # --------------------------------------------------------

    with col2:

        st.markdown("#### 🐙 Code Repositories")

        st.link_button(
            "💻 Explore My GitHub",
            "https://github.com",
        )

    st.write("")
    st.write("")

    st.success(
        "📩 **Direct Contact:** Please feel free to open "
        "a conversation or drop professional references "
        "through my social channels."
    )