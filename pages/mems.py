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


st.markdown("<h1 style='text-align: center;'><font color='black'>Just some v cute and cherished memories of us</font></h1>", unsafe_allow_html=True)

st.markdown("""
<font color='black'>
There will always be more, more than I can capture, more than I can remember, more than I can put down physically in front of us. Nevertheless, here are some that occupy my mind a lot <3
</font>
""",unsafe_allow_html=True)

st.markdown("""<h2 style='text-align: center;'><font color='black'>
September 1st, Our First Date
</font></h2>""", unsafe_allow_html=True)

st.video("images/sep1.mp4")
st.image("images/sep1.jpg")

st.markdown("""<h2 style='text-align: center;'><font color='black'>
September 12, You Gave Me Duck :)
</font></h2>""", unsafe_allow_html=True)

st.video("images/sep12.mp4")

st.markdown("""<h2 style='text-align: center;'><font color='black'>
September 13th, Cultural Night \n 
I've watched this video too many times and will continue to do so.
</font></h2>""", unsafe_allow_html=True)

st.image("images/sep13_1.jpg")
st.image("images/sep13_3.jpg")
st.video("images/sep13_2.mp4")

st.markdown("""<h2 style='text-align: center;'><font color='black'>
All yours love
</font></h2>""", unsafe_allow_html=True)

st.image("images/sep26.jpg")

st.markdown("""<h2 style='text-align: center;'><font color='black'>
27th September - My title comes from you 
</font></h2>""", unsafe_allow_html=True)

st.image("images/sep27.jpg")


st.markdown("""<h2 style='text-align: center;'><font color='black'>
October 4 - I remember my mom loved these.
</font></h2>""", unsafe_allow_html=True)

st.video("images/oct4.mp4")

st.markdown("""<h2 style='text-align: center;'><font color='black'>
October 13th, One of my favorite days ever (Sushi Date)
</font></h2>""", unsafe_allow_html=True)

st.image("images/oct13_1.jpg")
st.image("images/oct13_2.jpg")
st.image("images/oct13_3.jpg")
st.image("images/oct13_4.jpg")
st.image("images/oct13_5.jpg")
st.image("images/oct13_6.jpg")
st.video("images/oct13_7.mp4")
st.video("images/oct13_8.mp4")



st.markdown("""<h2 style='text-align: center;'><font color='black'>
October 26 - My first... Macaron
</font></h2>""", unsafe_allow_html=True)

st.video("images/oct26.mp4")


st.markdown("""<h2 style='text-align: center;'><font color='black'>
January 3 - We went to my friends birthday and I had so much fun with you there
</font></h2>""", unsafe_allow_html=True)

st.image("images/jan3.jpg")
st.image("images/jan3_1.jpg")

st.markdown("""<h2 style='text-align: center;'><font color='black'>
January 13 - My first HUCon with you
</font></h2>""", unsafe_allow_html=True)

st.image("images/jan13.jpg")
st.image("images/jan13_1.jpg")
st.image("images/jan13_2.jpg")


st.markdown("""<h2 style='text-align: center;'><font color='black'>
January 30 - Robert, my favorite animal
</font></h2>""", unsafe_allow_html=True)

st.video("images/jan30.mp4")


st.markdown("""<h2 style='text-align: center;'><font color='black'>
February 13 - I love this flower, thank you <3
</font></h2>""", unsafe_allow_html=True)

st.image("images/feb13.jpg")


st.markdown("""<h2 style='text-align: center;'><font color='black'>
February 14 - Invited everyone to simp
</font></h2>""", unsafe_allow_html=True)

st.video("images/feb14.mp4")


st.markdown("""<h2 style='text-align: center;'><font color='black'>
April 2 - I loved them so much, they were excellent 
</font></h2>""", unsafe_allow_html=True)

st.video("images/april2.mp4")

st.markdown("""<h2 style='text-align: center;'><font color='black'>
April 8 - A very cute drawing time
</font></h2>""", unsafe_allow_html=True)

st.video("images/april8.mp4")


st.markdown("""
<font color='black'>
These are just a very tiny amount of memories but ones I cherish very deeply. 
Here's to making more my love.
</font>
""",unsafe_allow_html=True)
