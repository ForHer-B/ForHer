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
st.markdown("<h1 style='text-align: center;'><font color='black'>Us before we were Us</font></h1>", unsafe_allow_html=True)

st.markdown("""
<font color='black'>
This was before 28th August 2023, all my friends telling me I've got a crush on you, I like you, I'm falling for you and me? Refusing to believe them. No matter how big the smile on my face. \n
I remember this day, April 28th (28 seems like a good day for us), I was happy when I left uni, you got me a gajra and I went to a wedding afterwards wearing it... I was teased by my sister and my cousins but, I was happy :) \n
</font>
""",unsafe_allow_html=True)

video_G = open("images/April28Gajra.mp4", "rb")
video_bytesG = video_G.read()

st.video(video_bytesG)

st.markdown("""
<font color='black'>
It was silly of me to not believe people who know me well. \n
I remember the first time I asked you if you liked me. It was... an interesting and nervous experience. I wouldn't have known what to do. Honestly, my friends tried to advise me. Don't be so upfront. I really don't get signals so I said, let's be straight up. \n
My goodness, I REALLY did not understand signals. I'm sure even now, there's many that pass over my head... From both, that time before we were dating and now too... \n
I remember, Welcome Evening I believe, we were sitting outside of reception, not where the stairs are but below them, close to the grass. I was wailing about me being single and then you, "You're husband material, that's why you don't have a girlfriend."... A minute later... "I'm looking for a husband." ... I really was blind huh? But look now, I've got someone I'm trying to turn into my wife ;) \n
I also remember you trying to show me how to rizz. Us sitting in courts, underneath the ledge. You asked me to look over my shoulder and tried to pull my face back. I resisted... A minute later... I need the 'pRaCtiCE' so I ask if I can do it to you randomly. You accept. I was blind to my crush on you too... \n
Also, biting the same leaf... I was completely and utterly blind... it was very "I have a crush on this person" activity to do by you :p \n
</font>
""",unsafe_allow_html=True)
st.image("images/welc_ev1.jpg")
st.image("images/welc_ev2.jpg")
st.video("images/welc_ev3.mp4")
st.markdown("""
<font color='black'>
Another thing about welcome evening, my drawing your eyeliner on, my hand so close to your face.... Just thinking about all this puts a massive smile on my face :) \n
Me going out of my way to get you cookies for your birthday... I don't know when the line between being good friends and being each others crushes was crossed... \n
Texting allll the time even though I never really texted people anymore...\n
This: \n
</font>
""",unsafe_allow_html=True)

st.image("images/Women_Error.jpg")

st.markdown("""
<font color='black'>
Well, you were right, I ended up with an entity :) \n
</font>
""",unsafe_allow_html=True)