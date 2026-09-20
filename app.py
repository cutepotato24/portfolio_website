import streamlit as st
import streamlit.components.v1 as components
import urllib.error
import urllib.request


def brand_logo(brand: str, color: str, size: int = 30):
    url = f"https://cdn.jsdelivr.net/npm/simple-icons@11.15.0/icons/{brand}.svg"
    try:
        svg = urllib.request.urlopen(url, timeout=15).read().decode("utf-8")
    except (urllib.error.HTTPError, urllib.error.URLError):
        return ""
    svg = svg.replace("<svg", f'<svg fill="{color}" color="{color}" style="width:{size}px;height:{size}px;display:block;"', 1)
    svg = svg.replace('fill="currentColor"', f'fill="{color}"')
    svg = svg.replace('fill="none"', f'fill="{color}"')
    svg = svg.replace('fill="#000000"', f'fill="{color}"')
    svg = svg.replace('fill="#000"', f'fill="{color}"')
    return svg


@st.dialog("Power BI dashboard", width="large")
def show_power_bi_picture(project):
    image_columns = st.columns([1, 20, 1])
    with image_columns[1]:
        st.image(f"assets/{project['file']}", caption=project["name"], use_container_width=True)
    if st.button("Hide picture", key=f"hide_{project['file']}"):
        st.session_state[f"show_{project['file']}"] = False
        st.rerun()


# 1. Page Configuration (Must be the first command)
st.set_page_config(
    page_title="Professional Portfolio",
    page_icon="🔷",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Pure charcoal, white, and electric-blue theme.
st.markdown(
    """
    <style>
        :root {
            --charcoal: #17191c;
            --charcoal-soft: rgba(34, 38, 43, 0.62);
            --white: #f5f7fa;
            --muted: #aeb6c2;
            --blue: #39a8ff;
            --blue-dark: rgba(13, 38, 56, 0.62);
            --border: #3a414a;
        }

        .stApp {
            background: var(--charcoal);
            color: var(--white);
        }

        [data-testid="stSidebar"] {
            background: rgba(17, 19, 21, 0.55) !important;
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

        [data-testid="stSidebar"] iframe {
            position: fixed;
            left: 0;
            bottom: 0;
            z-index: 999;
            width: 21rem !important;
            max-width: 100vw;
        }

        .main .block-container {
            max-width: 1000px;
            padding: 3rem 2.5rem 5rem;
            position: relative;
            z-index: 1;
        }

        .site-background {
            position: fixed;
            inset: 0;
            z-index: 0;
            pointer-events: none;
            overflow: hidden;
            background: rgba(23, 25, 28, 0.58);
        }

        .site-background::after {
            content: "";
            position: absolute;
            inset: 0;
            background: rgba(8, 11, 14, 0.58);
        }

        .site-background img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            opacity: 0.20;
        }

        .astronaut-background {
            position: fixed;
            top: 10vh;
            left: 5vw;
            z-index: 0;
            pointer-events: none;
            user-select: none;
            opacity: 0.10;
            filter: drop-shadow(0 0 18px rgba(57, 168, 255, 0.45));
            animation: astronaut-bounce 600s linear infinite;
        }

        .astronaut-background img {
            display: block;
            width: clamp(7rem, 14vw, 13rem);
            height: auto;
            transform-origin: center;
            animation: astronaut-float 180s ease-in-out infinite;
        }

        .astronaut-secondary {
            animation-delay: -150s;
        }

        @keyframes astronaut-float {
            0%, 100% {
                transform: translateY(0) rotate(-4deg);
            }
            50% {
                transform: translateY(-0.7rem) rotate(4deg);
            }
        }

        @keyframes astronaut-bounce {
            0% {
                top: 10vh;
                left: 5vw;
                transform: rotate(-12deg);
            }
            25% {
                top: 78vh;
                left: 88vw;
                transform: rotate(24deg);
            }
            50% {
                top: 16vh;
                left: 88vw;
                transform: rotate(112deg);
            }
            75% {
                top: 78vh;
                left: 5vw;
                transform: rotate(204deg);
            }
            100% {
                top: 10vh;
                left: 5vw;
                transform: rotate(348deg);
            }
        }

        @media (prefers-reduced-motion: reduce) {
            .site-background img {
                visibility: hidden;
            }

            .astronaut-background,
            .astronaut-background img {
                animation: none;
            }
        }

        h1, h2, h3, h4 {
            color: var(--white) !important;
        }

        .icon {
            color: var(--blue);
        }

        .skill-heading-icon {
            color: var(--muted) !important;
            opacity: 0.95;
        }

        .skill-badge-wrapper {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.8rem;
            min-height: 54px;
            margin-top: 0.6rem;
            align-items: center;
        }

        .skill-section-title {
            margin: 0;
            text-align: center;
        }

        .rdbms-row {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.8rem;
            margin: 1rem auto 0;
            max-width: 540px;
        }

        .skill-pill {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 38px;
            height: 38px;
            background: transparent;
            border: none;
            padding: 0;
            box-shadow: none;
            transition: transform 0.2s ease, opacity 0.2s ease;
            cursor: pointer;
            position: relative;
        }

        .skill-pill:hover {
            transform: translateY(-1px);
            opacity: 0.9;
        }

        .skill-pill::after {
            content: attr(data-tooltip);
            position: absolute;
            left: 50%;
            bottom: calc(100% + 0.45rem);
            transform: translateX(-50%) translateY(0.2rem);
            background: var(--charcoal-soft);
            border: 1px solid var(--border);
            border-radius: 3px;
            color: var(--white);
            font-size: 0.75rem;
            line-height: 1;
            padding: 0.45rem 0.55rem;
            pointer-events: none;
            opacity: 0;
            white-space: nowrap;
            transition: opacity 0.15s ease, transform 0.15s ease;
            z-index: 2;
        }

        .skill-pill:hover::after,
        .skill-pill:focus-visible::after {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        .skill-pill svg {
            width: 30px;
            height: 30px;
            display: block;
            background: transparent;
            vertical-align: middle;
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
            min-height: 126px;
            padding: 1.1rem 1rem;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.18);
        }

        [data-testid="stMetricLabel"],
        [data-testid="stMetricDelta"] {
            color: var(--muted) !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--white) !important;
            font-size: 2.25rem !important;
            font-weight: 800 !important;
            letter-spacing: 0 !important;
            line-height: 1.1 !important;
            text-shadow: 0 0 18px rgba(57, 168, 255, 0.22);
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--charcoal-soft);
            border: 1px solid var(--border);
            border-left: 3px solid var(--blue);
            border-radius: 3px;
            padding: 0.75rem 1rem;
        }

        [data-testid="stLinkButton"] {
            background: rgba(57, 168, 255, 0.82) !important;
            border: 0 !important;
            border-radius: 3px !important;
            color: #07131d !important;
            font-weight: 700 !important;
        }

        [data-testid="stLinkButton"]:hover {
            background: rgba(245, 247, 250, 0.86) !important;
            color: #07131d !important;
        }

        div[role="dialog"],
        [data-testid="stDialog"] {
            width: min(50vw, 800px) !important;
            max-width: 50vw !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }

        div[role="dialog"] [data-testid="stImage"],
        [data-testid="stDialog"] [data-testid="stImage"] {
            display: flex;
            justify-content: center;
        }

        div[role="dialog"] [data-testid="stImage"] img,
        [data-testid="stDialog"] [data-testid="stImage"] img {
            margin-left: auto;
            margin-right: auto;
        }

        .contact-card {
            min-height: 164px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 1.25rem;
            padding: 1.25rem;
            background: var(--charcoal-soft);
            border: 1px solid var(--border);
            border-top: 2px solid var(--blue);
            border-radius: 3px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.18);
        }

        .contact-card h4 {
            margin: 0;
            color: var(--white) !important;
        }

        .contact-action {
            display: block;
            padding: 0.65rem 0.8rem;
            background: rgba(57, 168, 255, 0.82);
            border-radius: 3px;
            color: #07131d !important;
            font-weight: 700;
            line-height: 1.3;
            text-align: center;
            text-decoration: none;
        }

        .contact-action:hover {
            background: rgba(245, 247, 250, 0.86);
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

st.markdown(
    """
    <div class="site-background" aria-hidden="true">
        <img src="https://i.pinimg.com/originals/cb/51/d4/cb51d4d903138dd276f63538e422c855.gif" alt="">
    </div>
    <div class="astronaut-background" aria-hidden="true">
        <img src="https://static.vecteezy.com/system/resources/thumbnails/077/495/720/small/floating-astronaut-icon-waving-in-zero-gravity-silhouette-free-png.png" alt="">
    </div>
    <div class="astronaut-background astronaut-secondary" aria-hidden="true">
        <img src="https://static.vecteezy.com/system/resources/thumbnails/077/495/720/small/floating-astronaut-icon-waving-in-zero-gravity-silhouette-free-png.png" alt="">
    </div>
    """,
    unsafe_allow_html=True,
)

# 2. Sidebar Structural Navigation
st.sidebar.markdown("## <span class='icon'>☰︎</span> Navigation", unsafe_allow_html=True)
page = st.sidebar.radio("Go to:", ["Profile Overview", "Core Projects", "Technical Skills", "Contact & Links"])

with st.sidebar:
    components.html(
        """
        <style>
            html, body {
                margin: 0;
                background: transparent;
                overflow: hidden;
            }

            .local-clock {
                box-sizing: border-box;
                padding: 0.45rem 0.75rem;
                color: #aeb6c2;
                font: 600 0.74rem/1.2 monospace;
                letter-spacing: 0.04em;
                text-transform: uppercase;
                white-space: nowrap;
            }

            .local-clock strong {
                color: #39a8ff;
                font-weight: 700;
            }
        </style>
        <div class="local-clock" id="local-clock" role="status" aria-live="polite">Detecting local time...</div>
        <script>
            const clock = document.getElementById("local-clock");
            const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
            const timeFormatter = new Intl.DateTimeFormat([], {
                hour: "numeric",
                minute: "2-digit",
                second: "2-digit",
                timeZoneName: "short"
            });

            function updateClock() {
                const location = timeZone || "your location";
                clock.innerHTML = "Local time <strong>" + timeFormatter.format(new Date()) + "</strong> · " + location;
            }

            updateClock();
            setInterval(updateClock, 1000);
        </script>
        """,
        height=42,
        scrolling=False,
    )

# --- PAGE 1: PROFILE OVERVIEW ---
if page == "Profile Overview":
    st.title("Hi, Thanks for visiting! ✦︎")
    st.subheader("I'm Harold, Analytics & vibe Software Engineer")

    st.info("⚡︎ I specialized in building automated data workflows and clean user experiences for data and business intelligence applications.")

    st.markdown("### Professional Profile")
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
    st.markdown("### Career Statistics")

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
    st.write(
        "Browse through an assortment of my recent professional applications. I am still updating my projects, and more projects will be added soon."
    )

    with st.expander("Personal Portfolio Website", expanded=False):
        st.caption("⚙︎ Tech Stack: `Python` | `Streamlit` | `CSS`")
        st.write("Designed and built this interactive portfolio website to present my professional profile, projects, technical skills, and contact links.")
        st.link_button("↗︎ View GitHub Repository", "https://github.com/cutepotato24/portfolio_website")

    st.write("")

    with st.expander("Airbnb dbt Project", expanded=False):
        st.caption("⚙︎ Tech Stack: `Snowflake` | `dbt` | `AWS S3`")
        st.write(
            "A data engineering project focused on ingesting and transforming Airbnb data from local files and external sources such as AWS S3 using Snowflake and dbt."
        )
        st.link_button("↗︎ View GitHub Repository", "https://github.com/cutepotato24/airbnb_dbt_project")

    st.write("")

    with st.expander("Tableau Data Visualizations", expanded=False):
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
                use_container_width=True,
            )
        with link_col2:
            st.link_button(
                "↗︎ Onyx Viz",
                "https://public.tableau.com/app/profile/john.harold.legaspi6572/viz/OnyxDataaugust2023DNAChallenge/Dashboard1",
                use_container_width=True,
            )

    st.write("")

    with st.expander("Power BI Data visualization", expanded=False):
        st.caption("⚙︎ Tools: `Power BI` | `Data Visualization` | `Dashboard Design`")
        st.write("Select a dashboard tile to view its screenshot.")

        power_bi_projects = [
            {
                "file": "Commercial_Revenue_PBI.png",
                "name": "Commercial Revenue",
                "description": "Tracks commercial revenue performance and highlights trends across the business.",
            },
            {
                "file": "Regional_Sales_PBI.png",
                "name": "Regional Sales",
                "description": "Compares sales performance across regions to reveal trends and growth opportunities.",
            },
            {
                "file": "US_Adidas_PBI.png",
                "name": "US Adidas",
                "description": "Explores Adidas sales in the United States across products, categories, and regions.",
            },
        ]

        project_columns = st.columns(2, gap="small")
        visible_projects = []
        for project_index, project in enumerate(power_bi_projects):
            with project_columns[project_index % 2]:
                with st.container(border=True):
                    st.markdown(f"### {project['name']}")
                    st.write(project["description"])
                    show_picture = st.checkbox("Show picture", key=f"show_{project['file']}")
                    if show_picture:
                        visible_projects.append(project)

        if visible_projects:
            show_power_bi_picture(visible_projects[0])

# --- PAGE 3: TECHNICAL SKILLS ---
elif page == "Technical Skills":
    st.title("Technical Know-Hows ⌘︎")
    st.write("A comprehensive breakdown of tools, programming languages, and engineering concepts I used throughout my career.")

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 class='skill-section-title'>Programming</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='skill-badge-wrapper'>
                <div class='skill-pill' data-tooltip='Python' title='Python' aria-label='Python' tabindex='0'>""" + brand_logo('python', '#3776AB') + """</div>
                <div class='skill-pill' data-tooltip='SQL' title='SQL' aria-label='SQL' tabindex='0'>""" + brand_logo('mysql', '#4479A1') + """</div>
                <div class='skill-pill' data-tooltip='HTML' title='HTML' aria-label='HTML' tabindex='0'>""" + brand_logo('html5', '#E34F26') + """</div>
                <div class='skill-pill' data-tooltip='CSS' title='CSS' aria-label='CSS' tabindex='0'>""" + brand_logo('css3', '#1572B6') + """</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown("<h3 class='skill-section-title'>Frameworks</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='skill-badge-wrapper'>
                <div class='skill-pill' data-tooltip='Streamlit' title='Streamlit' aria-label='Streamlit' tabindex='0'>""" + brand_logo('streamlit', '#FF4B4B') + """</div>
                <div class='skill-pill' data-tooltip='Python Libraries' title='Python Libraries' aria-label='Python Libraries' tabindex='0'>""" + brand_logo('python', '#3776AB') + """</div>
                <div class='skill-pill' data-tooltip='GitHub' title='GitHub' aria-label='GitHub' tabindex='0'>""" + brand_logo('github', '#FFFFFF') + """</div>
                <div class='skill-pill' data-tooltip='dbt' title='dbt' aria-label='dbt' tabindex='0'>""" + brand_logo('dbt', '#FF694A') + """</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<h3 class='skill-section-title'>Data Visualization</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='skill-badge-wrapper'>
                <div class='skill-pill' data-tooltip='Tableau' title='Tableau' aria-label='Tableau' tabindex='0'>""" + brand_logo('tableau', '#E97627') + """</div>
                <div class='skill-pill' data-tooltip='Power BI' title='Power BI' aria-label='Power BI' tabindex='0'>""" + brand_logo('powerbi', '#F2C811') + """</div>
                <div class='skill-pill' data-tooltip='Microsoft Excel' title='Microsoft Excel' aria-label='Microsoft Excel' tabindex='0'>""" + brand_logo('microsoftexcel', '#217346') + """</div>
                <div class='skill-pill' data-tooltip='Python' title='Python' aria-label='Python' tabindex='0'>""" + brand_logo('python', '#3776AB') + """</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown("<h3 class='skill-section-title'>Automation</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='skill-badge-wrapper'>
                <div class='skill-pill' data-tooltip='Python' title='Python' aria-label='Python' tabindex='0'>""" + brand_logo('python', '#3776AB') + """</div>
                <div class='skill-pill' data-tooltip='KNIME Analytics' title='KNIME Analytics' aria-label='KNIME Analytics' tabindex='0'>""" + brand_logo('knime', '#3B82F6') + """</div>
                <div class='skill-pill' data-tooltip='Snowflake' title='Snowflake' aria-label='Snowflake' tabindex='0'>""" + brand_logo('snowflake', '#29B5E8') + """</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    st.markdown("<h3 class='skill-section-title'>RDBMS</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='rdbms-row'>
            <div class='skill-pill' data-tooltip='Snowflake' title='Snowflake' aria-label='Snowflake' tabindex='0'>""" + brand_logo('snowflake', '#29B5E8') + """</div>
            <div class='skill-pill' data-tooltip='Oracle' title='Oracle' aria-label='Oracle' tabindex='0'>""" + brand_logo('oracle', '#F80000') + """</div>
            <div class='skill-pill' data-tooltip='BigQuery' title='BigQuery' aria-label='BigQuery' tabindex='0'>""" + brand_logo('googlebigquery', '#4285F4') + """</div>
            <div class='skill-pill' data-tooltip='MS SQL Server' title='MS SQL Server' aria-label='MS SQL Server' tabindex='0'>""" + brand_logo('microsoftsqlserver', '#CC2927') + """</div>
            <div class='skill-pill' data-tooltip='PostgreSQL' title='PostgreSQL' aria-label='PostgreSQL' tabindex='0'>""" + brand_logo('postgresql', '#4169E1') + """</div>
            <div class='skill-pill' data-tooltip='MySQL' title='MySQL' aria-label='MySQL' tabindex='0'>""" + brand_logo('mysql', '#4479A1') + """</div>
            <div class='skill-pill' data-tooltip='DBeaver' title='DBeaver' aria-label='DBeaver' tabindex='0'>""" + brand_logo('dbeaver', '#FFFFFF') + """</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown("<h3 class='skill-section-title'>Generative AI</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='skill-badge-wrapper'>
            <div class='skill-pill' data-tooltip='ChatGPT' title='ChatGPT' aria-label='ChatGPT' tabindex='0'>""" + brand_logo('openai', '#74AA9C') + """</div>
            <div class='skill-pill' data-tooltip='GitHub Copilot' title='GitHub Copilot' aria-label='GitHub Copilot' tabindex='0'>""" + brand_logo('githubcopilot', '#FFFFFF') + """</div>
            <div class='skill-pill' data-tooltip='Microsoft Copilot' title='Microsoft Copilot' aria-label='Microsoft Copilot' tabindex='0'>""" + brand_logo('microsoft', '#FFFFFF') + """</div>
            <div class='skill-pill' data-tooltip='Claude AI' title='Claude AI' aria-label='Claude AI' tabindex='0'>""" + brand_logo('anthropic', '#D97757') + """</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    st.markdown("### Areas of Focus")
    st.write("- **Data Architecture:** Designing scalable database management layouts.")
    st.write("- **Workflow Automation:** Replacing manual data pipelines with automated scripts.")
    st.write("- **Data Analysis & Metric Reporting:** Transforming data into reliable metrics, recurring reports, and actionable insights.")
    st.write("- **End-to-End Analytics Pipelines:** Managing the full-stack analytics workflow from source data and transformation through dashboards and reporting.")

# --- PAGE 4: CONTACT & LINKS ---
elif page == "Contact & Links":
    st.title("Establish Connection ✉︎")
    st.write("I am always interested in discussing new freelance agreements, corporate positions, or automation consulting.")

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="contact-card">
                <h4>Professional Networks</h4>
                <a class="contact-action" href="https://www.linkedin.com/in/jharold-legaspi/" target="_blank" rel="noopener noreferrer">↗︎ Go to LinkedIn</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="contact-card">
                <h4>Code Repositories</h4>
                <a class="contact-action" href="https://github.com/cutepotato24" target="_blank" rel="noopener noreferrer">↗︎ Explore My GitHub</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="contact-card">
                <h4>Direct Email Contact</h4>
                <a class="contact-action" href="https://mail.google.com/mail/?view=cm&fs=1&to=jllegaspicareers@gmail.com" target="_blank" rel="noopener noreferrer">↗︎ Email Me</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.success("✉︎ **Direct Contact:** Please feel free to open a conversation or drop professional references through my social channels.")
