import streamlit as st
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import time
from streamlit_echarts import st_echarts
import pytrends
from pytrends.request import TrendReq
import requests
import pandas as pd


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Instacart Dasboard", page_icon="🛒")

st.title('Instacart Dasboard 🛒')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)

st.header('Communication Strategy 📢')

colored_header(
    label="Historic Data - Repurchases",
    description="By days, clients & products",
    color_name="violet-70",
)


a = st.selectbox("Choose a Module", ("Days", "Products", "Hours"), index=None, placeholder="Choose an option")
