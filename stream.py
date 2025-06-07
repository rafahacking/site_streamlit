import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Teste')

#Texto
st.header('1. Textos e Títulos')
st.subheader('Subtítulo')
st.markdown('Markdown')
st.text("Testo simples")

#Entradas do usuário
nome = st.text_input("Digite seu Nome: ")
comentario = st.text_area("Comentário")

if len(nome) > 0:
    st.text(f"'O comentário do {nome} foi {comentario}'")

idade = st.number_input("Digite sua Idade: ", min_value=0, max_value=100, placeholder="Idade")
esporte = st.radio("Esporte: ", ["Futebol", "Basquete"])

teste_check = st.checkbox("Teste")

estado = st.selectbox("Selecione o Estado: ", ["SP", "MG", "RJ"], placeholder="Estado")

mult = st.multiselect("Filtre: ", ["Teste1", "Teste2"])

botao = st.button("Enviar")

if botao:
    st.success("Sua mensagem foi recebida")

st.header("Upload de arquivos")
arquivo = st.file_uploader("Envie um arquivo Excel", type=["xlsx"])

st.image("gato-desconfiado.PNG")

produtos = pd.Dataframe(
    {
        "Produto":["Computador", "Bicicleta", "Cadeira"],
        "Valor":[5000, 800, 900]

    }

)

st.dataframe(produtos)