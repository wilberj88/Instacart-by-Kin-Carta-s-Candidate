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

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(
    layout = 'wide',
    page_title = 'Instacart Dashboard Demo by Wilber Jimenez',
    page_icon="🛒"
)

with st.sidebar:
    image = Image.open('KinCartalogo.png')
    st.image(image, caption='Demo sourced by 🛒 Instacart DB and APIs of 🌧️ Open Weather and 🔎 Google Trends in Real Time 🏭 by candidate Wilber Jiménez Hernández')
  

st.title('Instacart real time Dasboard 🛒')
st st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True) 
st.markdown('<div style="text-align: left;">Hello World!</div>', unsafe_allow_html=True)
st.header('Marketing Decission´s Team')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)

st.header('Product Strategy 📦')

colored_header(
    label="Historic Data - Purchases",
    description="By days and hot & cold trends",
    color_name="violet-70",
)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Best Hour", "10:00", "20%")
col2.metric("Best Day", "Sunday", "33%")
col3.metric("Best Client", "ID 72.726", "25%")
col4.metric("Best Product", "ID 24.852", "17%")
