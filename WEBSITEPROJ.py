import streamlit as st
import time as t
import streamlit.components.v1 as com

st.markdown(
     f"""
     <style>
     .stApp {{
         background: url('https://i.postimg.cc/LsRVH6L5/3418448.jpg');
         background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
 )



#com.iframe('https://lottie.host/?file=cb4ab332-b345-4eab-b2c2-3b7f6548fb8f/UwN8mO3Dyv.json')
com.iframe('https://lottie.host/embed/a7643623-1ae2-48a5-9fef-ff821f4cb395/f55Squ40mg.json')
st.title("🤖 MAZE RUNNER 🤖")

#st.info("MEMBERS:\n 1.SHARVIN \n 2.ISHAAN")


a=st.file_uploader("Upload your image here")
if a!=None:
    with st.spinner('Uploading'):
        t.sleep(3)
    with com.iframe('https://lottie.host/?file=e64f72d2-705a-4cd2-9826-ef15e79a147a/qGfumu64bV.json'):
        t.sleep(3)
    # with st.image(r'https://i.postimg.cc/LXmxk2VP/Animation-1699159054281.gif',width=100):
    #     t.sleep(3)
    st.success("IMAGE HAS BEEN UPLOADED SUCCESSFULLY.")
