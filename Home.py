import streamlit as st
st.set_page_config(layout="wide")
#from streamlit_navigation_bar import st_navbar # type: ignore

#page = st_navbar(["Home", "Learn More", "Scanner", "About Me"])

st.sidebar.image("small.png", use_column_width=True)
with st.container():
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
    set_png_as_page_bg('back.png')

    #title
    col1,col2,col3 = st.columns(3)
    with col2:
        st.image("title2.png")

    #subheading
    subheading = '<p style="font-family:serif; color:Black; font-size: 30px;text-align: center;">A little introduction into the matter...</p>'
    st.markdown(subheading, unsafe_allow_html=True)

    #body
    st.write("A brain tumor is an abnormal growth of cells within the brain, which can disrupt its normal function. These growths can be benign (non-cancerous) or malignant (cancerous), and both types require attention due to the limited space in the skull.")
    subheading = '<p style="font-family:serif; color:Black; font-size: 30px;text-align: center;">Why Regular Checks Matter Once Symptoms are Displayed</p>'
    st.markdown(subheading, unsafe_allow_html=True)
    st.write("Early detection is crucial for improving outcomes. Brain tumours can cause serious issues like headaches, vision loss, or cognitive impairment. Once symptoms are displayed, by staying proactive and getting regular scans, potential tumours can be identified early, leading to more effective treatment and a better chance of recovery.")
    subheading = '<p style="font-family:serif; color:Black; font-size: 30px;text-align: center;">How Brain Tumor Scanners Work</p>'
    st.markdown(subheading, unsafe_allow_html=True)
    st.write("This website uses image classification technology to analyze MRI scans of the brain. In simple terms, this means that the system looks at the images and can tell whether a brain tumor is present by recognizing patterns that indicate cancer. The technology compares the scan with many others to identify abnormalities, providing quick and accurate results to help you get the care you need faster.")
    import streamlit as st

    #BUTTONS
    # m = st.markdown("""
    # <style>
    # div.stButton > button:first-child {
    #     background-color: rgb(36, 86, 135);
    # }
    # </style>""", unsafe_allow_html=True)
    co1, co2, co3, co4, co5 = st.columns([4,1,2,1,4])
    with co2:
        b = st.button("Try it for Free!")
    with co4:
        st.button("Learn More")
    
    
#footer
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #245687;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>© [2024] Brain Tumor Detection | Empowering early detection through accessible technology and information.</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
