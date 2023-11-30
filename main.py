import streamlit as st
from streamlit_option_menu import option_menu
import home, account, your_post, about
from PIL import Image

img = Image.open('profile-pic.png')
st.set_page_config(
        page_title="Mhark's Blog",
        page_icon=img
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



class MultiApp:

        def __init__(self):
            self.apps = []

        def add_app(self, title, func):

            self.apps.append({
                "title": title,
                "function": func
            })

        def run():
            # app = st.sidebar(
            with st.sidebar:        
                app = option_menu(
                    menu_title='Mharks Blog',
                    options=['Home','Recent Posts','Account','About'],
                    icons=['house-fill','chat-fill','person-circle','info-circle-fill'],
                    menu_icon='chat-text-fill',
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important","background-color":'black'},
            "icon": {"color": "white", "font-size": "23px"}, 
            "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},}
                    
                    )

            
            if app == "Home":
                home.app()
            if app == "Account":
                account.app()          
            if app == 'Recent Posts':
                your_post.app()
            if app == 'About':
                about.app()    
                       
        run()            
            
