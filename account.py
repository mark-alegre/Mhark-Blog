import streamlit as st

def app():
   with st.container():
     cal1, cal2 = st.columns(2)
     
     with cal1:
        st.image("profile-pic.png")
   
     with cal2:
       
        st.header("📝My Personal Info:")
        st.markdown("---")
        with open('account.css') as source_des:
         st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
        st.write("#")
        st.subheader("📝Full Name:")
        st.write(
            """
               - ✅ Mark Anthony Romero Alegre
            """
               )
        st.subheader("📝Age & Birthday:")
        st.write(
            """
               - ✅ 19 Years Old
               - ✅ May 5, 2004
            """
               )
        st.subheader("📝Address:")
        st.write(
            """
               - ✅ P1, Sico-sico, Gigaquit, Surigao Del Norte
              
            """
               )
   with st.container():
      social_media = {
         "Tiktok": "https://www.tiktok.com/@mhark.anthonie?lang=en",
         "Facebook": "https://www.facebook.com/markanthony.alegre.9279",
         "Github": "https://github.com/mark-alegre?tab=repositories",
         "Instagram": "https://www.instagram.com/markanthonyromeroalegre/",
      }
      st.write("#")
      cols = st.columns(len(social_media))
      for index, (platform, link) in enumerate(social_media.items()):
         cols[index].write(f"[{platform}]({link})")
   with st.container():
      st.markdown("---")
      st.subheader("📝School Attended:")
      st.write(
            """
               - ✅ Nuevo Campo Elementary School
               - ✅ Sisters of Mary Schools-Boystown Inc,.
               
              
            """
               )
      st.subheader("📝Work Experiences:")
      st.write(
            """
               - ✅ Work at LiteCloud Inc for 8 months as one of the Software Developer of the company
               - ✅ Work as IT personnel of Claver Cable TV for 3 months
               
              
            """
               )
      
         