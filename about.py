import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie 
def app():
     with st.container():
        with open('account.css') as source_des:
            st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
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
                        

                        lottie_coding = load_lottiefile("about.json")  # replace link to local lottie file
                        lottie_hello = load_lottieurl("https://lottie.host/22a4aa36-3fc0-4322-9c1d-dbe8ae6151ea/acWfpcTFII.json")

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
                st.write("#")
                st.markdown("<h1 style='text-align: center;'>About Mhark's Blog</h1>", unsafe_allow_html=True)       
            
            st.markdown("---")
            st.write(
                    """
                    - ✅ Welcome to  Mhark's Blog corner of the web, where passion meets information! I'm thrilled to have you here and share a bit about myself and the exciting features you'll find on this site.
                    
                    """
               )
            col1, col2 = st.columns(2)
            with col1:
                    st.write("#")
                    st.markdown("<h2 style='text-align: center;'>Who Am I?</h2>", unsafe_allow_html=True)
                    st.markdown("---")
                    st.write(
                            """
                            - ✅ I'm Mark Anthony Alegre, your friendly neighborhood enthusiast on a journey to explore and share interesting facets of life. 
                            
                            
                            - ✅ Whether it's discovering the latest trends, diving into the world of weather forecasting, or staying updated with current events, I'm here to make it an engaging experience for you.
                            """
                    )
           
            with col2:
                st.write("#")
                st.markdown("<h2 style='text-align: center;'>News Articles</h2>", unsafe_allow_html=True)
                st.markdown("---")
                st.write(
                        """
                       - ✅ Stay in the know with our curated selection of news articles. I believe in the power of information,
                        and here you'll find a variety of topics – from global headlines to niche interests. It's not just about the news; 
                        it's about fostering a community of informed individuals who appreciate the value of staying connected to the world.
                         """
                )
            st.write("#")
            st.markdown("<h2 style='text-align: center;'>Why Mhark's Blog?</h2>", unsafe_allow_html=True)
            st.markdown("---")
            st.write(
                    """
                    -
                    This website is more than just a digital space; it's a reflection of my curiosity and commitment to providing valuable content. I strive to create an online environment that's informative, user-friendly, and enjoyable. Your feedback is invaluable, so feel free to explore, engage, and let me know how I can enhance your experience.

                    Thank you for being a part of this journey. Here's to learning, exploring, and embracing the endless possibilities that the digital world offers.

                    Cheers,

                    Mark Anthony Alegre
                    """
            )
        
        st.markdown("---")    
        st.header(":mailbox: Get In Touch With Me!")
        contact_form = """
        <form action="https://formsubmit.co/mark.anthony.alegre05@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
                with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("about.css")