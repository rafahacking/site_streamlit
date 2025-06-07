import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Análise de Produtos",layout="wide")

# print(dataframe)
arquivo = st.file_uploader("Envie um arquivo Excel", type="xlsx")
st.button("Enviar arquivo")

if arquivo == None:
    st.text("Suba o arquivo")
else:

    dataframe = pd.read_excel(arquivo)

    maispesado = dataframe['Peso_Kg'].max()

    colfilter1, colfilter2 = st.columns(2)

    with colfilter1:
            minimo = st.number_input(label="Mínimo", label_visibility='visible',min_value=0,max_value=int(maispesado))

    with colfilter2:
            maximo = st.number_input(label="Máximo", label_visibility="visible",min_value=0,max_value=int(maispesado))

    filtrado = dataframe[(dataframe["Peso_Kg"] > minimo) & (dataframe["Peso_Kg"] < maximo) ]

    st.dataframe(filtrado)

    quantidade_produtos = len(filtrado)

    total_kg = filtrado["Peso_Kg"].sum()

    media_kg = filtrado["Peso_Kg"].mean()

    produto_categoria = filtrado.groupby("Categoria")["ID_Produto"].count().reset_index()

    st.title("Produtos em Estoque")

    col1, col2, col3 = st.columns(3)
    
    col1.metric("Total de Produtos: ", quantidade_produtos)

    col2.metric("Total em KIlos: ", total_kg)

    col3.metric("Media em Kilos: ", media_kg)

    st.bar_chart(data=produto_categoria,x= "Categoria",y="ID_Produto")