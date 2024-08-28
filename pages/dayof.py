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
st.markdown("<h1 style='text-align: center;'><font color='black'>The Day Of</font></h1>", unsafe_allow_html=True)

st.markdown("""
<font color='black'>
Let's start a few days before I asked you the question (Yes, I asked you out first before you could get the change to ask me out ;) I will always have that over you :p) \n
We were hugging at reception and then you did something you have NEVER done before, dap me up after a hug. I realized something was different. Why did you feel the need to show that our friendship was just a friendship... A person is defensive when they have something to hide... In your case, your crush on me :p. Hehehe I'm still smiling on the fact that you like me and have a crush on me. \n
I had doubt i n c r e a s e. So, I did the natural thing, I asked you the next day. \n
"Do you like me?" \n
"No... Do YOU like me?" \n
"No... But, if I were to date anyone it would be you" \n
"....We'll talk about this baad mei..." \n
Anyone in their right mind hearing the conversation and the actions before it would most certainly know that we liked each other.... \n
Nevertheless, I thought about your question over the weekend, If I like you. I thought to myself. \n
"Well, she doe hit all the criteria (what I held at the time), and I do feel an unusual amount of comfort around her, and I do go out of my way to spend time with her, and I do like talking to her, and I do like spending time with her, and she is pretty, and I feel really relaxed around her, time spent with her feels like a very excellent way to spend time, she doesn't fit in any category of people I've ever met, she make me feel happy whenever she's around.... O H.... I do like her .... I should tell her and see what we should do from there, in the name of being a better teammate and listening to other opinions on what to do next..." \n

Fast forward over the weekend, Monday, I sit like a toddler would and tell you how I feel. Absolutely insane. I genuinely never saw myself doing such a thing but with you, I feel right at home. I feel comfortable enough to sit like an idiot while I confess how I feel towards you. Sigh. I am glad though. Then you went on, consulted your friends, (by the way they congratulated me and gave me a hug that day), and then fast forward a year later, here we are. I absolutely love the story we have. Everytime I think about it, I smile. How could I not...
</font>
""",unsafe_allow_html=True)
