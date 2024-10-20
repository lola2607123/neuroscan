import streamlit as st
from ultralytics import YOLO
from PIL import Image
st.set_page_config(layout="wide")
# Load the model
@st.cache_resource
def models():
    mod = YOLO('best.pt') 
    return mod


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


with st.container():
    img = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])
    analyse = st.button('Analyze')

if analyse:
    if img is not None:
        img = Image.open(img)
        st.markdown('Image Visualization')
        st.image(img)
        model = models()
        res = model.predict(img)
        label = res[0].probs.top5
        conf = res[0].probs.top5conf
        conf = conf.tolist()
        st.write('Detected: ' + str(res[0].names[label[0]].title()))   
        st.write('Confidence level: ' + str(conf[0]))
