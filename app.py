import pandas as pd
import plotly.express as px
import streamlit as st

# lectura de datos
cars_data = pd.read_csv('vehicles_us.csv')

st.header('Listado vehicular')
st.write(cars_data)