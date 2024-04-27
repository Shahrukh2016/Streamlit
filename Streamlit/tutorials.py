import streamlit as st
import pandas as pd

st.title("Hi , I am Streamlit Web App ")
st.header("Hi, I am your header")
st.subheader("Hi, I am your subheader")
st.text("Hi,this is the sample text")
st.markdown("---")

st.markdown("**Hello** World")
st.markdown("[google](https://google.com)")
st.caption("Hi, I am your caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.json({"a":[1,2,3], "b": 5, "c": (10,20,30)})
code = '''
print("Hello Python")
def funct():
    return 0
'''
st.code(code, language = "python")
st.markdown("---")

## Lecture 5
st.write("[facebook](https://www.facebook.com)")
st.metric(label= "Wind Speed", value= "120ms⁻¹", delta="+1.5ms⁻¹")
st.table(pd.DataFrame({
    "Fruit": ["Mango", "Orange", "Apple", "Grapes"],
    "Colour": ["Yellow", "Orange", "Red", "Green"]
}))
st.dataframe(pd.DataFrame({
    "Fruit": ["Mango", "Orange", "Apple", "Grapes"],
    "Colour": ["Yellow", "Orange", "Red", "Green"]
}))
st.markdown("---")

## Lecture 6
st.image(image="SampleImage.png", caption="This is Overthinker", width=500)
st.audio(data="SampleAudio.mp3")
st.video(data= "SampleVideo.mp4")
st.markdown("---")

## Lecture 7
st.markdown("""
<style>
               .st-emotion-cache-6q9sum.ef3psqc4  
            {visibility: hidden},
</style>
""", unsafe_allow_html= True)
st.markdown("---")

## Lecture 8
bool = st.checkbox(label= "Have you cleared your SpaceX interview ? Check if Yes.")
if bool:
    st.write("Congratulations! Welcome to the SpaceX🚀")
else:
    st.write("Oops! Better luck next time.")

def change():
    print("changed")
bool = st.checkbox(label= "Have you cleared your Nasa interview ?", value= False, on_change=change)

def change():
    print(st.session_state.checker)
bool = st.checkbox(label= "Have you cleared your Nasa interview ?", value= False, on_change=change, key="checker")

radio_btn = st.radio(label="What is the next mission of Musk ?", options=("Mars", "AI Rockets", "Robots"))

def button_clicked():
    print("Button Clicked")
button = st.button("Click Me!",on_click= button_clicked)


singleselect = st.selectbox(label="Hi, how are you ?", options=("Fine", "Not Fine"))
st.write(singleselect)

multisleect = st.multiselect(label="Which is your favorate tech brand?", options=("Miscrosoft", "Amazon", "Apple"))
st.write(multisleect)
st.markdown("---")

## Lecture 9
st.title("Uploading files")
image = st.file_uploader(label="Please upload an image", type=["png", "jpg", "jpeg"])
if image is not None:
    st.image(image= image)

video = st.file_uploader(label="Please upload a video", type="mp4")
if video is not None:
    st.video(data= video)

## multiple files
images = st.file_uploader(label="Please upload multiple images", type=["png", "jpg", "jpeg"], accept_multiple_files= True)
if images is not None:
    for image in images:
        st.image(image= image)
st.markdown("---")

## Lecture 10
st.slider(label="This is a Slider", min_value=-50, max_value=+50,step=2)
st.text_input(label="Please write your sentence below:", max_chars=60)
st.text_area(label="Please write your paragraph below:")
st.date_input(label="Please enter your onboarding date:")
st.time_input(label="Please select the time of timer:")