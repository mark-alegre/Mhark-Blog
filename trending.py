import streamlit as st
import requests
from datetime import datetime , timedelta
import pandas as pd
import matplotlib.pyplot as plt
import time 

def app():
   

    
  
    # INSERT YOUR API  KEY WHICH YOU PASTED IN YOUR secrets.toml file 
    api_key =  st.secrets.get["api_key"]

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    

    # Function for LATEST WEATHER DATA
    def getweather(city):
        result = requests.get(url.format(city, api_key))     
        if result:
            json = result.json()
            #st.write(json)
            country = json['sys']['country']
            temp = json['main']['temp'] - 273.15
            temp_feels = json['main']['feels_like'] - 273.15
            humid = json['main']['humidity'] - 273.15
            icon = json['weather'][0]['icon']
            lon = json['coord']['lon']
            lat = json['coord']['lat']
            des = json['weather'][0]['description']
            res = [country, round(temp,1),round(temp_feels,1),
                    humid,lon,lat,icon,des]
            return res , json
        else:
            print("error in search !")


    # Let's write the Application

    st.header('Streamlit Weather Report')
    social_media = {
         "Visit OpenWeatherMap": "https://openweathermap.org/api",
      }
    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
         cols[index].write(f"[{platform}]({link})")   
   
    im1,im2 = st.columns(2)
    with im2:  
        image0 = 'openweather.png' 
        st.image(image0,use_column_width=True,caption = 'We will use Open Weather Map API as our Data Resource.')
    with im1:    
        image1 = 'weather.jpg'
        st.image(image1, caption='',use_column_width=True)
    with open('home.css') as source_des:
        st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
        st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        city_name = st.text_input(":green[Enter a city name]")
    with col2:  
            if city_name:
                    res , json = getweather(city_name)
                    #st.write(res)
                    st.success('Current: ' + str(round(res[1],2)))
                    st.info('Feels Like: ' + str(round(res[2],2)))
                    st.info('Humidity: ' + str(round(res[3],2)))
                    st.subheader('📍Status: ' + res[7])
                    web_str = "![Alt Text]"+"(http://openweathermap.org/img/wn/"+str(res[6])+"@2x.png)"
                    st.markdown(web_str)  
    st.write("#")    
    with st.container():
        st.write("---")
        with open('account.css') as source_des:
         st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
        st.title("🏢 About OpenWeather")
        st.write(
                    """
                    - ✅ OpenWeatherMap, commonly known as OpenWeather, 
                    is an online platform that provides comprehensive weather data and services. 
                    Users can access real-time weather information, forecasts,
                    and historical data for locations worldwide through APIs and other tools.
                    OpenWeather offers features such as geocoding, weather maps,
                    and specialized data like UV index and air quality. 
                    Its APIs are popular among developers for integration into applications and websites.
                    The platform caters to individuals, businesses, 
                    and researchers seeking accurate and up-to-date weather information.
                    It's advisable to check the official OpenWeather website for the latest features and offerings.
                    
                    """
               )
        social_media = {
         "Learn More": "https://openweathermap.org/about-us",
        }
        cols = st.columns(len(social_media))
        for index, (platform, link) in enumerate(social_media.items()):
            cols[index].write(f"[{platform}]({link})")
