import pandas as pd
import streamlit as st
import plotly.express as px

dados = pd.read_csv('C:/Users/cassi/projeto/vehicles.csv')

st.header('Dashboard de anúncios de carros')
st.write('Permite visualizar dados de anúncios')

hist_button = st.button('Cria Histograma')

if hist_button:
    st.write('Criando histograma de Kms dos veículos')
    fig = px.histogram(dados, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando gráfico de dispersão entre km e preço')
    fig = px.scatter(dados, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)