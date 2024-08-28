import streamlit as st
from PIL import Image
from numpy import asarray
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 
st.set_page_config(page_title="One Year Anniversary", page_icon="💖", initial_sidebar_state="collapsed")
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
st.markdown("<h1 style='text-align: center;'><font color='black'>Blessings on My Phone</font></h1>", unsafe_allow_html=True)
st.markdown("""
<font color='black'>

- The countless messages you send me that I star and re-read so so many times. \n
- My notes about you \n
- Your contact, I can reach you even if there's distance between us \n
- These (which there should be more of....): \n
</font>
""",unsafe_allow_html=True)

# Add Images of her here
st.image("images/b1.jpg")
st.image("images/b2.jpg")
st.image("images/b3.jpg")
st.image("images/b4.jpg")
st.image("images/b5.jpg")
st.image("images/b6.jpg")
st.image("images/b7.jpg")
st.image("images/b8.jpg")
st.image("images/b9.jpg")
st.image("images/b10.jpg")
st.image("images/b11.jpg")
st.image("images/b12.jpg")
st.image("images/b13.jpg")
st.image("images/b14.jpg")
st.image("images/b15.jpg")
st.image("images/b16.jpg")
st.image("images/b17.jpg")
st.image("images/b18.jpg")
st.image("images/b19.jpg")
st.image("images/b20.jpg")
st.image("images/b21.jpg")
st.image("images/b22.jpg")
st.image("images/b23.jpg")
st.image("images/b24.jpg")
st.image("images/b25.jpg")


st.markdown("""
<font color='black'>
Look my love, there's so many pictures of you I get to see and appreciate, all I'm saying is more (an infinite amount more) wouldn't hurt anyone \:p
But in all seriousness, I do appreciate and cherish the pictures I have of you and will all do so with the ones you decide to bless my phone with. It's something I have of you whenever you aren't around. I like looking at you...
.
.
.
Honestly... Gathering these pictures for this made me a little nervous... Seeing you again... You are ... Yeah, you make me nervous sometimes...

Here is another very good example of when you made me thora sa (🤏) nervous...
</font>
""",unsafe_allow_html=True)

st.image("images/nervous.jpg")
