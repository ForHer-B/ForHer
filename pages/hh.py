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


st.markdown("<h1 style='text-align: center;'><font color='black'>H*lding H*nds</font></h1>", unsafe_allow_html=True)

st.markdown("""
<font color='black'>
When what matters most to me is in the palm of my hand <3
</font>
""",unsafe_allow_html=True)

st.image("images/hh1.jpg")
st.image("images/hh2.jpg")
st.image("images/hh3.jpg")
st.image("images/hh4.jpg")
st.image("images/hh5.jpg")
