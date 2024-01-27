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
import matplotlib.pyplot as plt
import seaborn as sns

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Instacart Dasboard", page_icon="🛒")

st.title('Instacart Dasboard 🛒')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)

st.header('Product Strategy 📦')

colored_header(
    label="Historic Data - Purchases",
    description="By days and hot & cold trends",
    color_name="violet-70",
)


a = st.selectbox("Choose a Module", ("Days", "Products", "Hours"), index=None, placeholder="Choose an option")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Best Hour", "10:00", "20%")
col2.metric("Best Day", "Sunday", "33%")
col3.metric("Best Client", "ID 72.726", "25%")
col4.metric("Best Product", "ID 24.852", "17%")

df_orders =  pd.read_csv("data/Orders.csv", index_col=0)
st.write(df_orders)
