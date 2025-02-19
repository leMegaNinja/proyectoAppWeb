import pandas as pd
import plotly.express as px
import streamlit as st

# lectura de datos
cars_data = pd.read_csv('vehicles_us.csv')

st.header('Muestra del Listado vehicular')
st.write(cars_data.head(10))

# agregar compañia automotriz
#for i in range(len(cars_data)):
#    string1 = cars_data.loc[i]['model']
#    string2 = string1.split(' ')
#    cars_data.loc[i, ['manufacturer']] = string2[0]
# Esta parte afecta el tiempo de carga de la pagina, vamos a hacer otra cosa para el histograma.

# Primer histograma
st.header('El tipo de autos hay disponibles.')
fig = px.histogram(cars_data, x="type")
st.plotly_chart(fig, use_container_width=True)

st.write('¿Deseas ver un histograma de los colores que hay disponibles?')
# creación de botón
hist_button = st.button('Si')

if hist_button:
    fig = px.histogram(cars_data, x="paint_color")
    st.plotly_chart(fig, use_container_width=True)

# listado de casillas de verificación
st.header('Aquí tienes algunas otras gráficas que podrían interesarte')
pre_mod = st.checkbox("Precio x Año")
pre_con = st.checkbox("Precio x Condición")
pre_odo = st.checkbox("Precio x Kilometraje")

y1 = "price"

x1 = "model_year"
x2 = "condition"
x3 = "odometer"

if pre_mod:
    fig = px.scatter(cars_data, x = x1, y = y1)
    st.write('Precio de acuerdo al año del carro')
    st.plotly_chart(fig, use_container_width=True)

if pre_con:
    fig = px.scatter(cars_data, x = x2, y = y1)
    st.write('Precio de acuerdo a la condición')
    st.plotly_chart(fig, use_container_width=True)

if pre_odo:
    fig = px.scatter(cars_data, x = x3, y = y1)
    st.write('Precio de acuerdo al kilometraje')
    st.plotly_chart(fig, use_container_width=True)
