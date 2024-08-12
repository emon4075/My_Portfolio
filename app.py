import streamlit as st
import json
from streamlit_lottie import st_lottie

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
        🌱 I’m currently learning DSA
        💬 Ask me about C,C++,Java,Python,Git
        ⚡ Fun fact I Love Coding & Biryani more than anything else!
        """
)
st.markdown("---")
