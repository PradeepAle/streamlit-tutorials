import streamlit as st

st.write("Hello World: Getting Bore, Hello Brother!!")
st.title("Display Title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to  write headr use st.header()")
st.subheader("to write subheader use st.subheader()")
st.text("to write simple text use st.text()")
st.markdown("[streamlit](https://streamlit.io/)")
st.markdown("[streamlit cheatsheet](https://cheat-sheet.streamlit.app/)")
st.success("Success!")
st.info("Information")
st.warning("this is warning")
st.error("this is error")

from PIL import Image
img=Image.open("smj.jpg")
st.image(img,width=300,caption="Satmev Jayate")

video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://youtu.be/AqI97zHMoQw?si=rq7yIjze9oUc-IAs")

audio_file = open("song.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("Play")

st.header("Button Widgets")

if st.button("play"):
    st.text("Hello World")
    
if st.button("play2"):
    st.text("Enjoy Music")
    st.video("https://youtu.be/DeKLpgzh-qQ?si=ZZP8j8GQ9pQ9zYik")

if st.checkbox("Checkbox"):
    st.text("Checkbox selected")
    
