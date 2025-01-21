import pandas as pd
import plotly.express as px
import streamlit as st

# lectura de datos
cars_data = pd.read_csv('vehicles_us.csv')

st.header('Listado vehicular')
st.write(cars_data)

# agregar compañia automotriz
if not cars_data['manufacturer'] in cars_data:
    for i in range(len(cars_data)):
        string1 = cars_data.loc[i]['model']
        string2 = string1.split(' ')
        cars_data.loc[i, ['manufacturer']] = string2[0]

st.write('¿Deseas ver un histograma de las automotrices que hay disponibles?')
# creación de botón
hist_button = st.button('construir histograma')

if hist_button:
    fig = px.histogram(cars_data, x="manufacturer")
    st.plotly_chart(fig, use_container_width=True)

