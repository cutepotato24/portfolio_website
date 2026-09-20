import streamlit as st

st.set_page_config(page_title="Harold's Portfolio", layout="centered")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Profile", "Projects", "Skills", "Contact"])

if page == "Profile":
    st.title("Harold")
    st.subheader("Analytics and Software Engineer")
    st.write(
        "I build automated data workflows and software that turn complex data "
        "into clear, useful business information."
    )

    st.header("About")
    st.write(
        "I design reliable Python pipelines, data tools, and simple user "
        "experiences for organizations that need to work with data at scale."
    )

elif page == "Projects":
    st.title("Projects")

    st.header("Cloud-Native E-Commerce Analytics Tool")
    st.write("Python, Streamlit, Pandas, and Plotly")
    st.write("A dashboard for monitoring retail transactions and segmenting purchasing behavior.")
    st.markdown("[View Git Repository](https://github.com)")

    st.header("Automated Pipeline Scheduling Engine")
    st.write("Python, SQL, Docker, and AWS Lambda")
    st.write("An automated database validation worker that checks thousands of data points each day.")
    st.markdown("[Read Technical Documentation](https://github.com)")

elif page == "Skills":
    st.title("Skills")

    st.header("Programming")
    st.write("Python")
    st.write("SQL")
    st.write("HTML and CSS")

    st.header("Tools and Infrastructure")
    st.write("Streamlit")
    st.write("Pandas and NumPy")
    st.write("Git and GitHub")

    st.header("Focus Areas")
    st.write("Data architecture")
    st.write("Workflow automation")

elif page == "Contact":
    st.title("Contact")
    st.write("I am available for freelance work, engineering roles, and consulting.")
    st.write("LinkedIn: [jharold-legaspi](https://www.linkedin.com/in/jharold-legaspi/)")
    st.write("GitHub: [cutepotato24](https://github.com/cutepotato24)")
    st.write(
        "Email: [jllegaspicareers@gmail.com](https://mail.google.com/mail/?view=cm&fs=1&to=jllegaspicareers@gmail.com)"
    )
