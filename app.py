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


# Projects 📽️
st.header("Projects 📽️")
projectList = st.columns(spec=4, gap="small", vertical_alignment="center")
projectUrls = [
    "https://github.com/emon4075/Employee_Management",
    "https://github.com/emon4075/Data_Visualization_API",
    "https://github.com/emon4075/Q_SOLVE",
    "https://github.com/emon4075/Contact_Form",
]
try:
    with projectList[0]:
        if st.button("Employee MS", type="primary"):
            webbrowser.open(projectUrls[0], new=2)
    with projectList[1]:
        if st.button("Plotting API Data", type="primary"):
            webbrowser.open(projectUrls[1], new=2)
    with projectList[2]:
        if st.button("Question Solve", type="primary"):
            webbrowser.open(projectUrls[2], new=2)
    with projectList[3]:
        if st.button("Contact Form", type="primary"):
            webbrowser.open(projectUrls[3], new=2)
except:
    pass
else:
    st.text("")
    st.markdown("---")


# Articles ✍️
st.header("Articles ✍️")
articleList = st.columns(spec=2, gap="large", vertical_alignment="bottom")
articleUrls = [
    "https://medium.com/@mdabdullahemon4075/generate-ssh-key-and-setup-for-git-e5867bd2083a"
]
with articleList[0]:
    if st.button(label="SSH Key"):
        webbrowser.open(articleUrls[0], new=2)

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
