import streamlit as st
from PIL import Image

st.title("This content isn't allowed on YouTube!!!!")
st.subheader("PLZ TRY AT YOUR OWN RISK!!")
st.image("warning.jpg",width=300)

b=st.subheader("Are you 18+!!!")
a=st.radio("",("Non","YES","NO"))
if a=="Non":
    st.text("")
elif a=="YES":
    st.success("You have entered!!!")
    st.button('CLICK "#SHOW" TO SEE THE CONTENT')
    if st.button('#SHOW'):
        video_file = open('tomo.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        video_file.close()
else:
    st.warning("This video is only for 18+")
    img=Image.open('not.jpg')
    st.image(img,width=200)
    


