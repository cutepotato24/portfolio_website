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
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN PAGE
       ======================================================== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       NAVIGATION BUTTONS
       ======================================================== */

    div[data-testid="stHorizontalBlock"] {
        gap: 10px;
    }


    /* Navigation button */
    .nav-button button {
        width: 100% !important;

        min-height: 48px !important;

        border-radius: 12px !important;

        border: 2px solid #b5b5b5 !important;

        background-color: #d9d9d9 !important;

        color: #333333 !important;

        font-size: 15px !important;

        font-weight: 600 !important;

        box-shadow:
            0 2px 4px rgba(0, 0, 0, 0.10) !important;

        transition:
            all 0.2s ease !important;
    }


    /* Hover */
    .nav-button button:hover {
        background-color: #bcbcbc !important;

        border-color: #8f8f8f !important;

        color: #111111 !important;

        transform: translateY(-2px) !important;

        box-shadow:
            0 4px 8px rgba(0, 0, 0, 0.15) !important;
    }


    /* ========================================================
       ACTIVE NAVIGATION BUTTON
       ======================================================== */

    .active-nav button {
        width: 100% !important;

        min-height: 48px !important;

        border-radius: 12px !important;

        border: 2px solid #555555 !important;

        background-color: #707070 !important;

        color: white !important;

        font-size: 15px !important;

        font-weight: 700 !important;

        box-shadow:
            0 4px 8px rgba(0, 0, 0, 0.20) !important;
    }


    /* ========================================================
       PAGE TITLE
       ======================================================== */

    .page-title {
        margin-top: 25px;
    }


    /* ========================================================
       PROJECT CARDS
       ======================================================== */

    .project-card {
        padding: 20px;

        border: 1px solid #d0d0d0;

        border-radius: 14px;

        background-color: #fafafa;

        margin-bottom: 20px;

        box-shadow:
            0 2px 6px rgba(0, 0, 0, 0.06);
    }


    /* ========================================================
       MOBILE NAVIGATION
       ======================================================== */

    @media (max-width: 700px) {

        .nav-button button,
        .active-nav button {

            min-height: 42px !important;

            font-size: 13px !important;

            padding: 5px !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# NAVIGATION FUNCTION
# ============================================================

def navigation_button(label):

    if st.session_state.page == label:

        st.markdown(
            '<div class="active-nav">',
            unsafe_allow_html=True
        )

        clicked = st.button(
            label,
            key=f"nav_{label}"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="nav-button">',
            unsafe_allow_html=True
        )

        clicked = st.button(
            label,
            key=f"nav_{label}"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    if clicked:

        st.session_state.page = label

        st.rerun()


# ============================================================
# NAVIGATION BAR
# ============================================================

nav1, nav2, nav3, nav4 = st.columns(4)


with nav1:
    navigation_button("Profile Overview")


with nav2:
    navigation_button("Core Projects")


with nav3:
    navigation_button("Technical Skills")


with nav4:
    navigation_button("Contact & Links")


# ============================================================
# SEPARATOR
# ============================================================

st.markdown(
    """
    <div style="
        height: 1px;
        background-color: #d0d0d0;
        margin: 20px 0 25px 0;
    "></div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE 1 — PROFILE OVERVIEW
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
# PAGE 2 — CORE PROJECTS
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
# PAGE 4 — CONTACT & LINKS
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

The result

Instead of relying on st.tabs(), the navigation is now made from actual Streamlit buttons:

┌───────────────────┐  ┌─────────────────┐  ┌────────────────────┐  ┌───────────────────┐
│  Profile Overview │  │  Core Projects  │  │  Technical Skills  │  │  Contact & Links  │
└───────────────────┘  └─────────────────┘  └────────────────────┘  └───────────────────┘


The current page is dark gray, while the other navigation buttons are light gray with visible borders and rounded corners.

This approach is much more reliable than trying to override Streamlit's internal st.tabs() styling.