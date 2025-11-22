import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Análisis Exploratorio de Datos de Vehículos")
hist_button = st.button("Construir Histograma de Odómetro")

if hist_button:
    st.write('Histograma de Odómetro')

    fig = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig, use_container_width=True) # mostrar el histograma

scatter_button = st.button("Construir Gráfico de Dispersión de Precio vs Odómetro") 
if scatter_button:
    st.write('Grafico de dispersión Odometro vs Precio')

    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) # mostrar el gráfico de dispersión

table_button = st.button("Mostrar Tabla Resumida de Precio y Odómetro por Año del Modelo")
if table_button:
    st.write('Resumen del precio promedio y el odómetro promedio por año del modelo')

    grouped_data = (car_data
                    .groupby(by = ['model_year'])
                    .agg({'price':'mean', 'odometer':'mean'})
                    .reset_index(drop=False)
                    .sort_values(by=['model_year'], ascending=False)
                    .set_index(pd.Index(range(1, len(car_data['model_year'].unique()))))) 
    
    st.dataframe(grouped_data)