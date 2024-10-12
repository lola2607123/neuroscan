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
    st.image("aboutitle.png")




col3,col4= st.columns(2)

with col4:
    st.write('''Welcome to my website! My name is Sri Gupta, and I'm working on a brain tumor detection scanner that uses artificial intelligence (AI) to analyze MRI scans. This project aims to enhance the accuracy and speed of brain tumor detection, which is crucial for timely treatment and better patient outcomes.

I started this project because I recognized the challenges associated with early detection of brain tumors. Many cases are diagnosed at advanced stages, which can limit treatment options. By implementing AI technology, I hope to streamline the detection process, making it more efficient for healthcare professionals. The goal is not just to provide a tool but also to contribute to the broader conversation about how technology can improve healthcare practices.''')
with col3:
    st.image("https://static.vecteezy.com/system/resources/previews/006/195/212/original/woman-or-girl-symbol-line-icon-stroke-graphics-pictogram-for-web-design-quality-outline-symbol-concept-premium-mono-linear-beautiful-simple-concise-logo-vector.jpg", width=400)

st.write("Through this website, I aim to share valuable information and resources related to brain tumor detection and the role of AI in medicine. I believe that as technology continues to evolve, it can play a significant role in enhancing medical practices. I hope you find the content here informative and useful as we explore the intersection of technology and healthcare together. Thank you for visiting!")