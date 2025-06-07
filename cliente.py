import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Clientes",layout='wide')

df = pd.read_excel("Clientes.xlsx")

st.title("Dashboard de Clientes")

st.subheader("Prévia dos dados")

st.dataframe(df)

st.subheader("Métricas")
st.text(f"Quantidade de clientes:{len(df)}")

st.subheader("Gráfico")
quantidade_estado = df.groupby("Estado")["ID_Cliente"].count().reset_index()

st.bar_chart(data=quantidade_estado,x="Estado",y="ID_Cliente")