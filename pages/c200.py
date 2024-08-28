import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 

st.set_page_config(page_title="One Year Anniversary", page_icon="💖", initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none;
    }
</style>
""",
    unsafe_allow_html=True,
)

with st.container():
    col3213, col321, col34, col444 = st.columns([20,40,40,60])
    with col3213:
        if st.button("Back", key="fsdahkfashjkaf"):
            st.switch_page("main.py")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe0e9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'><font color='black'>Number 1</font></h1>", unsafe_allow_html=True)


st.markdown("""
<font color='black'>
That day, the mix of nervousness, curiosity, excitedness and somehow comfort at the same time. I wanted to just leave a "😏" emoji here but nah. It was..IS so much deeper. It's a reminder of how you're my first. I replay that day... a lot. It's so ethereal. The teases from days before leading up to it. My heart racing everytime you got too close (it still does to this day). No one else has this power over me. It's in your eyes. In your presence. I'll go to war and never quit but in front of you? I surrender completely. 
It's nice to go along this flow of thoughts. These thoughts of you. Comfort. Excitedness. A bit of nervousness. It's all just... beautiful. Of course it is, it's related to you my love <3
</font>
""",unsafe_allow_html=True)