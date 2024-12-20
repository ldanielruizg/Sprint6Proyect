import pandas as pd
import plotly.express as px 
import streamlit as st
car_data = pd.read_csv('notebooks/vehicles_us.csv')
st.header('Cuadro de Mandos de Anuncios de Ventas de Coches')
st.write("Configuración del servidor:")
st.write("Headless:", st.config.get_option("server.headless"))
st.write("Port:", st.config.get_option("server.port"))
st.write("Server Address:", st.config.get_option("browser.serverAddress"))
st.write("Server Port:", st.config.get_option("browser.serverPort"))
hist_button = st.button('Construir histogramas')
if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')
    hist_fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(hist_fig, use_container_width=True)
scatter_button = st.button('Construir grafico de dipsersion')
if scatter_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    scatter_fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(scatter_fig, use_container_width=True)
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construccion de un histograma para la columna odometro')
    hist_fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(hist_fig, use_container_width=True)
build_scatter = st.checkbox('Construir un grafico de dispersion')
if build_scatter:
    st.write('Construccion de un grafico de dispersion para el kilometraje y el precio')
    scatter_fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(scatter_fig, use_container_width=True)