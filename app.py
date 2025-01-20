import pandas as pd
import plotly.express as px
import streamlit as st

# lectura de datos
cars_data = pd.read_csv('vehicles_us.csv')
print(cars_data.head())

# crear un histograma
fig = px.histogram(cars_data, x="model_year")
fig.show()

# crear un gráfico de dispersión
