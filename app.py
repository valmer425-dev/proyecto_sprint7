import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Análisis Exploratorio de Datos de Vehículos")
hist_button = st.button("Construir Histograma de Odómetro")

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig, use_container_width=True) # mostrar el histograma

scatter_button = st.button("Construir Gráfico de Dispersión de Precio vs Odómetro") 
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) # mostrar el gráfico de dispersión