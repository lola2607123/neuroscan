import streamlit as st
st.set_page_config(layout="wide")
st.sidebar.image("small.png", use_column_width=True)
#background picture
import base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .main {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: local;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
set_png_as_page_bg('background.png')


col1,col2,col3 = st.columns(3)
with col2:
    st.image("scantitle.png")


m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(255, 255, 255);text-align:center;
}
</style>""", unsafe_allow_html=True)

b = st.button("Upload your MRI")