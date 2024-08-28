pip install --upgrade streamlit
import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 
import base64
st.set_page_config(page_title="One Year Anniversary", page_icon="💖", initial_sidebar_state="collapsed")

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

if "button1" not in st.session_state:
    st.session_state.button1 = 0
if "button2" not in st.session_state:
    st.session_state.button2 = 0
if "button3" not in st.session_state:
    st.session_state.button3 = 0
if "button4" not in st.session_state:
    st.session_state.button4 = 0
if "button5" not in st.session_state:
    st.session_state.button5 = 0
if "button6" not in st.session_state:
    st.session_state.button6 = 0
if "button7" not in st.session_state:
    st.session_state.button7 = 0
if "button8" not in st.session_state:
    st.session_state.button8 = 0
if "button9" not in st.session_state:
    st.session_state.button9 = 0

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


# st.audio(audio_bytes, format="audio/ogg",loop=True)
# Title Header
st.markdown("<h1 style='text-align: center;'><font color='black'>To my love</font></h1>", unsafe_allow_html=True)

# Paragraph
st.markdown("""
<font color='black'>
Hello my love, I hope you're have a good day. This website is just a part of your actual gift.
Only at the end will you find your gift. In the meantime, here is a little walkthrough of how we got here. My point of view, my thoughts and how I feel. 
It may take some time. \n
Go through at your own pace. It's all just for you. \n
I hope you like it my love <3 \n
Also, now is the time to open the wrapped gift :) (It'll come in handy when you reach the actual)
(Apologies if the color/palette/design bit for the website does not work together...)
</font>
""",unsafe_allow_html=True)

# Date Header
# col5, col6, col7, col8 = st.columns([60, 60, 60, 60])

if st.session_state.button1 == 0:
    st.markdown("""
    <style>     
    .element-container:has(#button-after1)  + div button {
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
    <div id="button-1"></div>
    """, unsafe_allow_html=True)
    st.markdown('<div id="button1"> </div> <span id="button-after1"></span>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>     
    .element-container:has(#button-after1)  + div button {
        padding: 10px 10px;
        background-color: #e05780;
        color: #522e38;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        /* margin-left: 10px;   Add margin on the left */
        /* margin-right: 10px;  Add margin on the right */
    }
    </style>
    <div id="button-1"></div>
    """, unsafe_allow_html=True)
    st.markdown('<div id="button1"> </div> <span id="button-after1"></span>', unsafe_allow_html=True)

if st.button("Pre-Dating", use_container_width=True):
    st.session_state.button1 = 1
    st.switch_page("pages/predating.py")
if st.session_state.button2 == 0:
    st.markdown("""
    <style>     
    .element-container:has(#button-after2)  + div button {
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
    st.markdown('<div id="button2"> </div> <span id="button-after2"></span>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>     
    .element-container:has(#button-after2)  + div button {
        padding: 10px 10px;
        background-color: #e05780;
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
    st.markdown('<div id="button2"> </div> <span id="button-after2"></span>', unsafe_allow_html=True)
if st.button("August 28th, 2023", use_container_width=True):
    st.session_state.button2 = 1
    st.switch_page("pages/dayof.py")
if st.session_state.button3 == 0:
    st.markdown("""
    <style>     
    .element-container:has(#button-after3)  + div button {
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
    st.markdown('<div id="button2"> </div> <span id="button-after3"></span>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>     
    .element-container:has(#button-after3)  + div button {
        padding: 10px 10px;
        background-color: #e05780;
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
    st.markdown('<div id="button2"> </div> <span id="button-after3"></span>', unsafe_allow_html=True)
if st.button("C200", use_container_width=True):
    st.session_state.button3 = 1
    st.switch_page("pages/c200.py")
if st.session_state.button4 == 0:
    st.markdown("""
    <style>     
    .element-container:has(#button-after4)  + div button {
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
    st.markdown('<div id="button2"> </div> <span id="button-after3"></span>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>     
    .element-container:has(#button-after4)  + div button {
        padding: 10px 10px;
        background-color: #e05780;
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
    st.markdown('<div id="button2"> </div> <span id="button-after4"></span>', unsafe_allow_html=True)

if st.button("Blessings On My Phone", use_container_width=True):
    st.session_state.button4 = 1
    st.switch_page("pages/blessings.py")


if st.session_state.button5 == 0:
    st.markdown("""
    <style>     
    .element-container:has(#button-after5)  + div button {
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
    st.markdown('<div id="button2"> </div> <span id="button-after5"></span>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>     
    .element-container:has(#button-after5)  + div button {
        padding: 10px 10px;
        background-color: #e05780;
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
    st.markdown('<div id="button2"> </div> <span id="button-after5"></span>', unsafe_allow_html=True)

if st.button("Some Cute Memories", use_container_width=True):
    st.session_state.button5 = 1
    st.switch_page("pages/mems.py")


if st.session_state.button6 == 0:
    st.markdown("""
    <style>     
    .element-container:has(#button-after7)  + div button {
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
    st.markdown('<div id="button2"> </div> <span id="button-after7"></span>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>     
    .element-container:has(#button-after7)  + div button {
        padding: 10px 10px;
        background-color: #e05780;
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
    st.markdown('<div id="button2"> </div> <span id="button-after7"></span>', unsafe_allow_html=True)

if st.button("H* H*", use_container_width=True):
    st.session_state.button7 = 1
    st.switch_page("pages/hh.py")

if st.session_state.button6 == 0:
    st.markdown("""
    <style>     
    .element-container:has(#button-after6)  + div button {
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
    st.markdown('<div id="button2"> </div> <span id="button-after6"></span>', unsafe_allow_html=True)
else:
    st.markdown("""
    <style>     
    .element-container:has(#button-after6)  + div button {
        padding: 10px 10px;
        background-color: #e05780;
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
    st.markdown('<div id="button2"> </div> <span id="button-after6"></span>', unsafe_allow_html=True)

if st.button("The Big Secret", use_container_width=True):
    st.session_state.button6 = 1
    st.switch_page("pages/final.py")
