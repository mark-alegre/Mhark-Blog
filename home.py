import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def app():
    with open('home.css') as source_des:
        st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Hey There👋 Welcome To Mhark's Blog🎸</h1>", unsafe_allow_html=True)
    st.markdown("---")
    cols1, cols2 = st.columns([1,3])
        
    with cols1:
            def load_lottiefile(filepath: str):
                with open(filepath, "r") as f:
                    return json.load(f)


            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
            

            lottie_coding = load_lottiefile("weatherAnimation.json")  # replace link to local lottie file
            lottie_hello = load_lottieurl("https://lottie.host/5da1dffa-b69b-4b92-9d42-dd9a8246fae9/qIla7ft2xX.json")

            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low", # medium ; high
                height=None,
                width=None,
                key=None,
            )
    with cols2:
        
        st.markdown("<h2 style='text-align: center;'>☁️Today's Weather☁️</h2>", unsafe_allow_html=True)
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            col1.metric("Temperature", "70 °F", "1.2 °F")
            col2.metric("Wind", "9 mph", "-8%")
            col3.metric("Humidity", "86%", "4%")
            
            
    c1, c2 = st.columns([3,1])
    
    
    with c1:
        st.markdown("---")      
        st.markdown("<h2 style='text-align: center;'>🎬Select Category To Watch a Video🎬</h2>",unafe_allow_html=True)
        
    col1, col2, col3 = st.columns(3)
        
    v1 = col1.button("Coding Videos💻")
    if v1:
            with st.container():
        
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                video1 = 'Download.mp4'
                video2 = 'Download (1).mp4'
                

                # Set the width and height of the videos
                video_width = 200
                video_height = 200

                # Create a two-column layout
                col1, col2,  = st.columns(2)

                # Display the first video in the first column
                col1.video(video1, format="Download.mp4", start_time=0)

                # Display the second video in the second column
                col2.video(video2, format="Download (1).mp4", start_time=0)
                
                
        
    v2 = col2.button("Dance Videos🕺")
    if v2:
            with st.container():
                
            
            
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                video5 = 'Download (2).mp4'
                video6 = 'Download (3).mp4'

                # Set the width and height of the videos
                video_width = 200
                video_height = 200

                # Create a two-column layout
                col1, col2, = st.columns(2)

            
                # Display the first video in the first column
                col1.video(video5, format="Download (4).mp4", start_time=0)
                
                # Display the first video in the first column
                col2.video(video6, format="Download (5).mp4", start_time=0)

        
    v3 = col3.button("Playing Guitar🎸")
    if v3:
            with st.container():
                
            
            
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                video5 = 'Download (4).mp4'
                video6 = 'Download (5).mp4'

                # Set the width and height of the videos
                video_width = 200
                video_height = 200

                # Create a two-column layout
                col1, col2, = st.columns(2)

            
                # Display the first video in the first column
                col1.video(video5, format="Download (4).mp4", start_time=0)
                
                # Display the first video in the first column
                col2.video(video6, format="Download (5).mp4", start_time=0)
    with c2:     
        def load_lottiefile(filepath: str):
                    with open(filepath, "r") as f:
                        return json.load(f)


        def load_lottieurl(url: str):
                    r = requests.get(url)
                    if r.status_code != 200:
                        return None
                    return r.json()
                

        lottie_coding = load_lottiefile("video.json")  # replace link to local lottie file
        lottie_hello = load_lottieurl("https://lottie.host/9297aa80-b9e7-47ae-94d7-540808770c53/sRpSuCfjWa.json")

        st_lottie(
                    lottie_hello,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="low", # medium ; high
                    height=None,
                    width=None,
                    key=None,
            )
        