import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import numpy as np
import pandas as pd
import time 
#from datetime import time
import plotly.graph_objects as go
import pydeck as pdk
import folium
from streamlit_folium import st_folium
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import streamlit.components.v1 as com
import sqlite3 as sq3
import pandas.io.sql as pds
from PIL import Image
import seaborn as sns

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(
    layout = 'wide',
    page_title = 'Instacart Dashboard Demo by Wilber Jimenez',
    page_icon="🛒"
)

with st.sidebar:
    image = Image.open('KinCartalogo.png')
    st.image(image, caption='Demo sourced by 🛒 Instacart DB and APIs of 🌧️ Open Weather and 🔎 Google Trends in Real Time 🏭 by candidate Wilber Jiménez Hernández')
  
colA, colB = st.columns(2)
colA.title('Instacart real time Dashboard 🛒')
colB.title(' Marketing Decission´s Team')

colX, colY, colZ = st.columns(3)
colY.header('Key Performance Indicators')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Best Hour", "10:00", "20%")
col2.metric("Best Day", "Sunday", "33%")
col3.metric("Best Client", "ID 72.726", "25%")
col4.metric("Best Product", "ID 24.852", "17%")

colX, colY, colZ = st.columns(3)
colY.header('Strategies 🗺️ & Tactics 🔫')


     
col5, col6, col7 = st.columns(3)
with col5:
     with st.container(border=True):
        colored_header(
            label="Products 📦",
            description="By days and hot & cold trends",
            color_name="violet-70",
            )
        df_orders =  pd.read_csv("data/Orders.csv", index_col=0)
        st.dataframe(df_orders['order_hour_of_day'])
        
       
                   
        
with col6:
    with st.container(border=True):
        colored_header(
            label="Offers 🏷️",
            description="By days and hot & cold trends",
            color_name="violet-70",
            )
        
with col7:
    with st.container(border=True):
        colored_header(
            label="Communications 📢",
            description="By days and hot & cold trends",
            color_name="violet-70",
            )





st.subheader('In real time monitoring at:')
current_time = time.ctime()
st.write(current_time)
