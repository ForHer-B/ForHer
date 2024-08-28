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


st.markdown("<h1 style='text-align: center;'><font color='black'>Your actual gift</font></h1>", unsafe_allow_html=True)

st.markdown("""
<font color='black'>
My beloved, this is the actual gift for you. I hope you like it. \n
(Don't forget the present if you haven't opened it yet)
</font>
""",unsafe_allow_html=True)


st.markdown("""
    <style>     
    .element-container:has(#button-after99)  + div button {
        padding: 10px 10px;
        background-color: #ff9ebb;
        color: #522e38;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        /* margin-left: 10px;   Add margin on the left */
        /* margin-right: 10px;  Add margin on the right */
    }
    </style>
    <div id="button-2"></div>
    """, unsafe_allow_html=True)
st.markdown('<div id="button2"> </div> <span id="button-after99"></span>', unsafe_allow_html=True)
st.link_button("Enjoy meri jaan <3", "https://youtube.com/playlist?list=PLHiSDXNH_PdWbEStnEFtWdRUyviFFDkm1&si=qFBsN-Gq0yoCROWb")
