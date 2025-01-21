import pandas as pd
import plotly.express as px
import streamlit as st

# lectura de datos
cars_data = pd.read_csv('vehicles_us.csv')

st.header('Listado vehicular')
st.write(cars_data)

# agregar compañia automotriz
for i in range(len(cars_data)):
    string1 = cars_data.loc[i]['model']
    string2 = string1.split(' ')
    cars_data.loc[i, ['manufacturer']] = string2[0]

st.write('¿Deseas ver un histograma de las automotrices que hay disponibles?')
# creación de botón
hist_button = st.button('Si')

if hist_button:
    fig = px.histogram(cars_data, x="manufacturer")
    st.plotly_chart(fig, use_container_width=True)

# listado de casillas de verificación
st.header('Aquí tienes algunas otras gráficas que podrían interesarte')
pre_mod = st.checkbox("Precio x Año")
pre_con = st.checkbox("Precio x Condición")
pre_odo = st.checkbox("precio de acuerdo a su Kilometraje")
mod_tra = st.checkbox("Transmisión con los años")

y1 = "price"
y2 = "transmission"

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
    fig = px.bar(cars_data, x = x3, y = y1)
    fig.show()

if mod_tra:
    fig = px.bar(cars_data, x = x1, y = ['manual', 'automatic', 'other'], title = "Tipo de transmisión con el pasar de los años")
    fig.show()
    