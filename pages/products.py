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
from PIL import Image

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Instacart Dasboard", page_icon="🛒")

with st.sidebar:
    image = Image.open('data/KinCartalogo.png')
    st.image(image, caption='Demo sourced by 🛒 Instacart DB and APIs of 🌧️ Open Weather and 🔎 Google Trends in Real Time 🏭 by candidate Wilber Jiménez Hernández')
    with st.expander("See Documentation"):
        df_orders =  pd.read_csv("data/Orders.csv", index_col=0)
        st.subheader("Data")
        st.write(df_orders)
        st.subheader("Sources")
   

st.title('Instacart Dasboard 🛒')
current_time = time.ctime()
st.write("In real time monitoring at: ", current_time)

st.header('Product Strategy 📦')

colored_header(
    label="Historic Data - Purchases",
    description="By days and hot & cold trends",
    color_name="violet-70",
)


a = st.selectbox("Choose a module", ("All", "Days", "Products", "Hours"), index=None, placeholder="Select one")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Best Hour", "10:00", "20%")
col2.metric("Best Day", "Sunday", "33%")
col3.metric("Best Client", "ID 72.726", "25%")
col4.metric("Best Product", "ID 24.852", "17%")



meta_zona_1 = 10290
meta_zona_2 = 11986
meta_zona_3 = 11368
meta_zona_4 = 14018
meta_zona_5 = 14036
meta_zona_6 = 5241
meta_zona_7 = 3112
meta_zona_8 = 110
meta_zona_9 = 7338

col5, col6, col7 = st.columns(3)
with col5:
    
    meta = 35000
    st.subheader("Sales Yesterday Vs Today")
    option = {
    "xAxis": {
        "type": "category",
        "data": ["Hour_7", "Hour_8", "Hour_9", "Hour_10", "Hour_11", "Hour_12", "Hour_13"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [meta*0.1, meta*0.2, meta*0.35, meta*0.5, meta*0.75, meta*0.9, meta], "type": "line"},
        {"data": [meta*0.15, meta*0.25, meta*0.4, meta*0.55, meta*0.75, meta*0.9, meta], "type": "line"},
    ],
    }
    st_echarts(
        options=option, height="300px",
    )
with col6:
    st.subheader("Goal Sales Today: by currently hour and whole day")
    col6a, col6b = st.columns(2)
    with col6a:
        acelerometro2 = {
            "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
            "series": [
                {
                    "name": "Pressure",
                    "type": "gauge",
                    "axisLine": {
                        "lineStyle": {
                            "width": 10,
                        },
                    },
                    "progress": {"show": "true", "width": 10},
                    "detail": {"valueAnimation": "true", "formatter": "{value}"},
                    "data": [{"value": 50, "name": "By Hour"}],
                }
            ],
        }
        st_echarts(options=acelerometro2)
    with col6b:
        acelerometro1 = {
            "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
            "series": [
                {
                    "name": "Pressure",
                    "type": "gauge",
                    "axisLine": {
                        "lineStyle": {
                            "width": 10,
                        },
                    },
                    "progress": {"show": "true", "width": 10},
                    "detail": {"valueAnimation": "true", "formatter": "{value}"},
                    "data": [{"value": 30, "name": "By Day"}],
                }
            ],
        }
    
        st_echarts(options=acelerometro1)
     
with col7:
    st.subheader("Sales by days last week")
    options = {
            "title": {"text": "🧱"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
            },
            "legend": {"data": ["Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]},
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "23:59"],
                }
            ],
            "yAxis": [{"type": "value"}],
            "series": [
                {
                    "name": "Thursday",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                },
                  {
                    "name": "Wednesday",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                },
                  {
                    "name": "Tuesday",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                },
                  {
                    "name": "Monday",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                },
                  {
                    "name": "Sunday",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                },
            ],
        }
    st_echarts(options=options, height="300px")



