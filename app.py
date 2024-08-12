import streamlit as st
import json
from streamlit_lottie import st_lottie
import webbrowser


# Page Config
st.set_page_config(page_icon="goat.png", page_title="Portfolio | Emon")


# Hide Streamlit style elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


# Welcome Animation
animation = None
try:
    with open("welcome.json") as source:
        animation = json.load(source)
except Exception as e:
    pass


# Plotting The Head
col_1, col_2 = st.columns(2, gap="small")
with col_1:
    st.header("My Portfolio 💻")
    st.text("")
    st.text("")
    st.text("🐐 Md Abdullah Al Mamun Emon")
    st.text("😒 A CS Student")
    st.text("💊 A Passionate Tech Addict")
    st.text("⛑️ Leader @CU_Legends_V1")
    st.text("🎓 A Proud CSECUian")
with col_2:
    if animation:
        st_lottie(animation, width=300, height=300)
    else:
        pass

st.markdown("---")


# About Me
st.header("About Me 😎")
st.text(
    """👋 Greetings!
        I'm Md. Abdullah Al Mamun Emon, a dedicated Computer Science and 
        Engineering student with an insatiable curiosity for technology 
        and an unwavering passion for football.
        
        🔭 I’m currently working on Problem Solving
        🌱 I’m currently learning DSA & Arduino
        💬 Ask me about C,C++,Java,Python,Git
        ⚡ Fun fact I Love Coding & Biryani more than anything else!
        """
)
st.markdown("---")


# Skills
st.header("Skills 💪")
skills = {
    "Languages ✨": ["C", "CPP", "Java", "Python"],
    "Tools 🔨": ["Git", "GitHub", "Linux", "LaTeX"],
    "Editor ⌨️": ["VS Code", "NVim", "Zed"],
}
st.json(skills, expanded=False)
st.markdown("---")


# Custom CSS to remove link styles
no_style_link = """
<style>
a.no-style-link {
    text-decoration: none;
    color: inherit;
}
a.no-style-link:hover {
    color: #3A1078; /* Optional: Add a hover color if you want */
}
</style>
"""

# Apply the CSS
st.markdown(no_style_link, unsafe_allow_html=True)

# Projects 📽️
st.header("Projects 📽️")
projectList = st.columns(4, gap="small")
projectUrls = [
    "https://github.com/emon4075/Employee_Management",
    "https://github.com/emon4075/Data_Visualization_API",
    "https://github.com/emon4075/Q_SOLVE",
    "https://github.com/emon4075/Contact_Form",
]

with projectList[0]:
    if st.button("Employee MS"):
        st.markdown(
            '<a href="https://github.com/emon4075/Employee_Management" class="no-style-link" target="_blank">View Source Code</a>',
            unsafe_allow_html=True,
        )
with projectList[1]:
    if st.button("Plotting API Data"):
        st.markdown(
            '<a href="https://github.com/emon4075/Data_Visualization_API" class="no-style-link" target="_blank">View Source Code</a>',
            unsafe_allow_html=True,
        )
with projectList[2]:
    if st.button("Question Solve"):
        st.markdown(
            '<a href="https://github.com/emon4075/Q_SOLVE" class="no-style-link" target="_blank">View Source Code</a>',
            unsafe_allow_html=True,
        )
with projectList[3]:
    if st.button("Contact Form"):
        st.markdown(
            '<a href="https://github.com/emon4075/Contact_Form" class="no-style-link" target="_blank">View Source Code</a>',
            unsafe_allow_html=True,
        )

# Articles ✍️
st.header("Articles ✍️")
articleList = st.columns(2, gap="large")
articleUrls = [
    "https://medium.com/@mdabdullahemon4075/generate-ssh-key-and-setup-for-git-e5867bd2083a"
]

with articleList[0]:
    if st.button("SSH Key"):
        st.markdown(
            '<a href="https://medium.com/@mdabdullahemon4075/generate-ssh-key-and-setup-for-git-e5867bd2083a" class="no-style-link" target="_blank">Read The Article</a>',
            unsafe_allow_html=True,
        )


st.markdown("---")


# Social Media Links
st.header("Social 🌐")

cp = st.columns(spec=3, gap="medium", vertical_alignment="center")
with cp[0]:
    st.markdown(
        "[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/emon4075)"
    )
with cp[1]:
    st.markdown(
        "[![CodeChef](https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white)](https://www.codechef.com/users/mdabdullahemon)"
    )
with cp[2]:
    st.markdown(
        "[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/mdabdullahemon4075/)"
    )

media = st.columns(spec=3, gap="medium", vertical_alignment="center")
with media[0]:
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/emon4075/)"
    )
with media[1]:
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/emon4075)"
    )
with media[2]:
    st.markdown(
        "[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@mdabdullahemon4075)"
    )
st.text("")
st.markdown("---")


# Contact Form
st.header("Say Hello 🫂")
st.text("")

contact, animie = st.columns(spec=2, gap="small", vertical_alignment="center")
with contact:
    with st.form("My Form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        f_name = col1.text_input(label="First Name", placeholder="First")
        l_name = col2.text_input(label="Last Name", placeholder="Last")
        email = st.text_input(label="Your Mail", placeholder="you_mail@example.com")
        message = st.text_area(
            label="Message", placeholder="Love is blind 😙", max_chars=200
        )

        submitted = st.form_submit_button("Submit")

        if submitted:
            if f_name == "" or l_name == "" or message == "" or email == "":
                st.warning("Please fill out all fields.")
            else:
                st.success("Form submitted successfully!")
                res = f"""
                <div style="text-align: center;">
                    <form action="https://formsubmit.co/66fe6238339c6f0fc2fd4814f28b2478" method="POST">
                        <input type="hidden" name="First Name" value="{f_name}">
                        <input type="hidden" name="Last Name" value="{l_name}">
                        <input type="hidden" name="Message" value="{message}">
                        <input type="hidden" name="Email" value="{email}">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="submit" value="Confirm" style="
                            background-color: #D1E9F6;
                            border: none;
                            color: black;
                            padding: 10px 20px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            margin: 4px 2px;
                            cursor: pointer;
                            border-radius: 4px;">
                    </form>
                </div>
                """
                st.markdown(res, unsafe_allow_html=True)

with animie:
    with open(r"waiting.json") as source:
        animation = json.load(source)
    st_lottie(animation, width=350, height=300)

st.markdown("---")


# Footer
footer = """
<style>
.footer {
    position: justify;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: #3A1078;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
}
</style>
<div class="footer">
    <p>Made with 💖 by Emon</p>
    <p>©️2024</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
