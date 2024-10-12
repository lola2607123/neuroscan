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
#title
#col1,col2,col3 = st.columns(3)
#with col2:
    #st.image("titl.png")

c1, c2, c3, c4, c5 = st.columns([2,2,4,2,2])
with c1:
    st.image("right.png", width=200)
with c3:
    st.image("titl.png")
with c5:
    st.image("left.png", width=200)

import streamlit as st

col1, col2, col3= st.columns(3)

with col1:
    st.header("Types")
    st.write('''Benign brain tumors grow slowly and do not spread to other parts of the body, but they can still cause problems. As they grow, they take up space in the skull and press against important areas of the brain, potentially leading to symptoms like headaches, seizures, and trouble with movement or speech. Though they aren't cancerous, benign tumors can still be serious and sometimes require surgery to remove.''')
    st.image("https://www.researchgate.net/publication/340698597/figure/fig2/AS:881305088696325@1587130915259/The-brain-tumor-classification-into-benign-and-malignant-tumors_Q320.jpg")
    st.write('''Malignant brain tumors, or brain cancers, are more aggressive. They grow quickly and can invade surrounding brain tissue, making them harder to treat. Symptoms of malignant tumors are similar to those of benign ones but can progress faster. Treatment options include surgery, radiation therapy, and chemotherapy. Early detection is important, as it can increase the chances of successful treatment and reduce long-term effects.''')

with col2:
    st.header("Primary & Secondary")
    st.write('''Brain tumors are classified into two broad categories: primary and secondary. Primary brain tumors start in the brain itself, while secondary tumors (also called metastatic tumors) begin in other parts of the body and spread to the brain. Within primary tumors, there are different types based on the kind of cells involved. Gliomas, which form in the brain’s glial cells, are the most common. Subtypes of gliomas include astrocytomas, oligodendrogliomas, and ependymomas, each affecting different types of glial cells. Meningiomas are tumors that form in the meninges, the protective layers surrounding the brain and spinal cord. They are often benign but can still cause complications by pressing on brain structures. Medulloblastomas are another type of primary brain tumor, often seen in children, and they originate in the cerebellum.

Secondary brain tumors occur when cancer from other parts of the body, like the lungs, breasts, or skin, spreads to the brain. These tumors are always malignant because they come from other cancers. Treatment for secondary brain tumors often focuses on treating the primary cancer first, but they may require separate treatment to address the brain metastasis.''')
    st.image("https://www.researchgate.net/publication/340698597/figure/fig1/AS:881305088704517@1587130915235/The-brain-tumor-classification-into-primary-and-secondary-brain-tumors.jpg")
with col3:
    co1,co2 = st.columns(2)
    with co1:
        st.header("Stats")
        st.image("https://www.sdbtf.org/wp-content/uploads/2021/01/2021-SDBTF-Infographic-1.png", width=150)
    with co2:
        st.header(" ")
        st.write('''Brain tumors are relatively rare compared to other types of cancer, but they still have a significant impact on global health. In the United States alone, around 24,000 people are diagnosed with a brain or spinal cord tumor each year. Of these, about one-third are malignant (cancerous), while the rest are benign (non-cancerous). Gliomas, the most common type of malignant brain tumor, account for around 80% of all malignant brain tumors in adults.''')
    st.write('''Meningiomas, which are often benign, make up about 30% of all brain tumors. While survival rates vary depending on the type of tumor and how early it's detected, the overall 5-year survival rate for malignant brain tumors is around 36%, but this improves significantly for benign tumors, where many patients live long, healthy lives after treatment. However, brain tumors are still the leading cause of cancer-related deaths in children, highlighting the need for continued research and better treatments.''')

