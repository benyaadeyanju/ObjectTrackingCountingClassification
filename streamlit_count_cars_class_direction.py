#Benya Adeyanju Jamiu
# To run use
# conda activate YOLOR_streamlit
# streamlit run streamlit_count_cars_class_direction.py

from yolor_count_cars_class_direction import *

import tempfile
import cv2

import streamlit as st


def main():
    
    #title
    st.title('Object Tracking Dashboard YOLOR')
    
    #side bar title
    st.sidebar.title('Settings')
    
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 400px;
        margin-left: -400px;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    st.sidebar.markdown('---')
    confidence = st.sidebar.slider('Confidence',min_value=0.0, max_value=1.0, value = 0.25)
    st.sidebar.markdown('---')

    save_img = st.sidebar.checkbox('Save Video')
    enable_GPU = st.sidebar.checkbox('enable GPU')
    enable_webcam = st.sidebar.checkbox('enable webcam')
#####
    enable_stream = st.sidebar.checkbox('enable stream')
    if enable_stream:
        enable_webcam = False
        url_name = st.sidebar.text_input("Enter your URL_stream", "Type here...")

        if (st.sidebar.button('Submit')):
            url_stream = url_name.title()
            st.sidebar.success(url_stream)
        else :   url_stream = "https://cdn-004.whatsupcams.com/hls/hr_pula01.m3u8"
    else : url_stream = "https://cdn-004.whatsupcams.com/hls/hr_pula01.m3u8"
#####


    custom_classes = st.sidebar.checkbox('Use Custom Classes')
    assigned_class_id = []
    if custom_classes:
        assigned_class = st.sidebar.multiselect('Select The Custom Classes',list(names),default='person')
        for each in assigned_class:
            assigned_class_id.append(names.index(each))

    video_file_buffer = st.sidebar.file_uploader("Upload a video", type=[ "mp4", "mov",'avi','asf', 'm4v' ])

    DEMO_VIDEO = 'test.mp4'
    DEMO_VIDEO = 'Videos/Cars_on_highway_3.mp4'

    tfflie = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)


    ##We get our input video here

    if not video_file_buffer:
        vid = cv2.VideoCapture(DEMO_VIDEO)
        tfflie.name = DEMO_VIDEO
        dem_vid = open(tfflie.name,'rb')
        demo_bytes = dem_vid.read()

        st.sidebar.text('Input Video')
        st.sidebar.video(demo_bytes)

    else:
        tfflie.write(video_file_buffer.read())
        # print("No Buffer")
        dem_vid = open(tfflie.name,'rb')
        demo_bytes = dem_vid.read()
    
        st.sidebar.text('Input Video')
        st.sidebar.video(demo_bytes)


    print(tfflie.name)
    
    stframe = st.empty()
    
    st.markdown("<hr/>", unsafe_allow_html=True)
    kpi1, kpi2, kpi3 = st.columns(3) #st.columns(3)

    st.markdown("<hr/>", unsafe_allow_html=True)
    kpi4, kpi5 = st.columns(2)  # st.columns(2)

    st.markdown("<hr/>", unsafe_allow_html=True)
    kpi6, kpi7 = st.columns(2)  # st.columns(2)

    st.markdown("<hr/>", unsafe_allow_html=True)
    kpi8, kpi9 = st.columns(2)  # st.columns(2)

    st.markdown("<hr/>", unsafe_allow_html=True)
    kpi10, kpi11 = st.columns(2)  # st.columns(2)


    with kpi1:
        st.markdown("**Frame Rate**")
        kpi1_text = st.markdown("0")

    with kpi2:
        st.markdown("**Tracked Objects**")
        kpi2_text = st.markdown("0")

    with kpi3:
        st.markdown("**Width**")
        kpi3_text = st.markdown("0")

    with kpi4:
        st.markdown("**Counted Cars to North**")
        kpi4_text = st.markdown("0")

    with kpi5:
        st.markdown("**Counted Cars to South**")
        kpi5_text = st.markdown("0")

    with kpi6:
        st.markdown("**Counted Trucks to North**")
        kpi6_text = st.markdown("0")

    with kpi7:
        st.markdown("**Counted Trucks to South**")
        kpi7_text = st.markdown("0")

    with kpi8:
        st.markdown("**Counted Busses to North**")
        kpi8_text = st.markdown("0")

    with kpi9:
        st.markdown("**Counted Busses to South**")
        kpi9_text = st.markdown("0")

    with kpi10:
        st.markdown("**Counted Motorcycles to North**")
        kpi10_text = st.markdown("0")

    with kpi11:
        st.markdown("**Counted Motorcycles to South**")
        kpi11_text = st.markdown("0")


    st.markdown("<hr/>", unsafe_allow_html=True)

    # call yolor 
    #load_yolor_and_process_each_frame(tfflie.name, enable_GPU, confidence, assigned_class_id, #kpi1_text, kpi2_text, kpi3_text, stframe)

    load_yolor_and_process_each_frame(enable_stream, url_stream, enable_webcam, tfflie.name, enable_GPU, confidence, assigned_class_id, kpi1_text, kpi2_text, kpi3_text,
                                      kpi4_text, kpi5_text, kpi6_text, kpi7_text, kpi8_text, kpi9_text, kpi10_text, kpi11_text,stframe)
    
    st.text('Video is Processed')
    vid.release()
if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass


