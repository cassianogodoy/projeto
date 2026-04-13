import pandas as pd
import streamlit as st
import plotly.express as px

dados = pd.read_csv('vehicles.csv')

st.header("Dashboard de anúncios de carros")

st.write(dados.head())

hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Histograma da quilometragem")
    fig = px.histogram(dados, x="odometer")
    st.plotly_chart(fig)

scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Relação entre KM e preço")
    fig = px.scatter(dados, x="odometer", y="price")
    st.plotly_chart(fig)