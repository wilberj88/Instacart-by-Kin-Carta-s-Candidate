import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import numpy as np
import pandas as pd
import time as ts
from datetime import time
import plotly.graph_objects as go
import pydeck as pdk
import folium
from streamlit_folium import st_folium
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import streamlit.components.v1 as com

if "symbols_list" not in st.session_state:
    st.session_state.symbols_list = None
    
st.set_page_config(
    layout = 'wide',
    page_title = '🛒 Instacart Dashboard Demo'
)

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
    </style>
    """, unsafe_allow_html = True
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)


title_col, emp_col, btc_col, eth_col, xmr_col, sol_col = st.columns([2,0.2,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Instacart 🛒 Dashboard<br>Marketing Team</p>', unsafe_allow_html = True)

with btc_col:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Best Hour</p><p class="price_details">10:00h</p>', unsafe_allow_html = True)
       
with eth_col:
    with st.container(border=True):
        #eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">Best Day<br></p><p class="price_details">Sunday</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container(border=True):
        #xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">Best Client<br></p><p class="price_details">ID 72.726</p>', unsafe_allow_html = True)

with sol_col:
    with st.container(border=True):
        #sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">Best Product<br></p><p class="price_details">ID 24852</p>', unsafe_allow_html = True)



params_col, chart_col, data_col = st.columns([0.7,1.6,1.1])

with params_col:
    
    with st.form(key = 'params_form'):
        
        st.markdown(f'<p class="params_text">FILTERS', unsafe_allow_html = True)
                
        tipo_empresa = st.selectbox("Selecciona tipo de empresa:", ("S.L.", "S.A.", "S.L.L.", "Holding", "Comunidades de bienes", "Cooperativas", "Asociaciones", "Autónomos", "Emprendedores", "Particulares"), index=None, placeholder="Choose an option")
        
        servicios_contables_internacionales = st.selectbox("Selecciona tipo de servicio contable internacional:", ("Reporting", "Estados Financieros", "Informes Casa Matriz", "Auditorías de Control Interno"), index=None, placeholder="Choose an option")
        
        servicios_contables_outsourcing_gerencial = st.selectbox("Selecciona tipo de servicio contable outsourging gerencial necesitas:", ("Asistencia a Justa de Socios", "Análisis de Estados Financieros", "Atención Entidades Bancarias", "Estrategia Corporativa"), index=None, placeholder="Choose an option")

        a = st.slider("Indica nivel mínimo de facturación anual", 0, 100000, 5000)
        st.divider()
        update_chart = st.form_submit_button('Update chart')
        
        if update_chart:
           

            with chart_col:

                with st.container(border=True):
                    fig1 = go.Figure(data=[go.Sankey(
                            node = dict(
                                pad = 15,
                                thickness = 20,
                                line = dict(color = "black", width = 0.5),
                                label = ["Gastos Mensuales", "Necesidades", "Entretenimiento", "Inversiones", "Vivienda", "Estudio", "Alimentación", "Transporte", "Entretenimiento", "Viajes", "Acciones", "Activos", "Criptomonedas", "Bonos"],
                                color = "red"
                                ),
                            link = dict(
                            source = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
                            target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                            value = [50, 20, 30, 10, 20, 10, 22, 22, 10, 14, 10, 10, 10]
                            ))])
                        
                    fig1.update_layout(title_text="Usos promedio de tu presupuesto💰", font_size=12)
                    st.plotly_chart(fig1, theme="streamlit")

                                        
                    my_grid2 = grid(3, vertical_align="bottom")
                    my_grid2.button("Ranking Mejores Clientes", use_container_width=True)
                    my_grid2.button("Ranking Mejores Proveedores", use_container_width=True)
                    my_grid2.button("Ranking Peores Deudores", use_container_width=True)

                    st.markdown('<p class="dashboard_title">🌎 🔎</p>', unsafe_allow_html = True)
                    com.html("""
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2902.6990909515926!2d-1.9868735087859841!3d43.320558199425605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd51a551be27a135%3A0x61b266d5c1a5f46e!2sPl.%20de%20Guip%C3%BAzcoa%2C%2016%2C%2020004%20San%20Sebasti%C3%A1n%2C%20Gipuzkoa%2C%20Espa%C3%B1a!5e0!3m2!1ses!2sco!4v1704724179680!5m2!1ses!2sco" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    """, height=300, scrolling=True)
                 
                       
                    
            with data_col:
                st.header('Recomendaciones de acciòn YA')
                current_time = ts.ctime()
                st.write("In real time monitoring at: ", current_time)
                st.write('EN TODA ESPAÑA')

                col1, col2 = st.columns(2)
                with col1:
                    st.subheader('Plan A')
                    st.write('Decir en Galicia que con este clima es mejor vivir asegurado')
                with col2:
                    st.subheader('Plan B')
                    st.write('Decir en Galicia que con este clima es mejor vivir con abogado')
                df = pd.DataFrame(
                    {
                        "name": ["Contable", "Financiero", "Fiscal"],
                        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                        "stars": [random.randint(0, 1000) for _ in range(3)],
                        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                    }
                )
                st.dataframe(
                    df,
                    column_config={
                        "name": "Servicios",
                        "stars": st.column_config.NumberColumn(
                            "Github Stars",
                            help="Number of stars on GitHub",
                            format="%d ⭐",
                        ),
                        "url": st.column_config.LinkColumn("Link App URL"),
                        "views_history": st.column_config.LineChartColumn(
                            "Ventas (past 30 days)", y_min=0, y_max=5000
                        ),
                    },
                    hide_index=True,
                )
                a = st.button('PREDICCIÓN DE DESEMPEÑO EN ENGAGEMENT')
             
                st.write('Plan A: 5%; Plan B: 4,5%')
            
                data_df = pd.DataFrame(
                    {
                        "name": ["Laboral", "Legal", "Mercantil"],
                        "apps": [
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
                        ],
                        "sales": [
                            [0, 4, 26, 80, 100, 40],
                            [80, 20, 80, 35, 40, 100],
                            [10, 20, 80, 80, 70, 0],
                        ],
                        "Performance": [200, 550, 1000],
                    }
                )                
                st.dataframe(
                    data_df,
                    column_config={
                        "name": "Suscripciones",
                        "apps": st.column_config.ImageColumn(
                            "Web por Servicio", help="Streamlit app preview screenshots"
                        ),
                        "sales": st.column_config.BarChartColumn(
                            "Ventas (last 6 months)",
                            help="The sales volume in the last 6 months",
                            y_min=0,
                            y_max=100,
                        ),
                        "Performance": st.column_config.ProgressColumn(
                            "Performance",
                            help="The sales volume in USD",
                            format="$%f",
                            min_value=0,
                            max_value=1000,
                        ),
                    },
                    hide_index=True,
                )
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Ingresos", "70%", "40%")
                col2.metric("Gastos", "30%", "-82%")
                col3.metric("Rentabilidad", "16%", "43%")
                col4.metric("Rotación Personal", "87%", "78%")
                   
                st.caption("By Wilber Jimenez Hernandez")
            
           

                              
