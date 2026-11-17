import pandas as pd
import openpyxl
import streamlit as st
import plotly.express as px

df_bruto = pd.read_excel("dados-educacao.xlsx")

df = df_bruto.loc[df_bruto["escolaridade"]=="Mestrado"]
df = df.iloc[0:,[1,3]]
df_cont_masc = df.loc[df["genero"]=="Masculino"].count(0)
df_cont_fem = df.loc[df["genero"]=="Feminino"].count(0)

st.set_page_config(page_title="Prova Felipe Cornélio", layout="wide")
st.title("Distribuição de Mestrados por gênero")
st.header("tabela bruta")
st.dataframe(df)

st.header("diferença")
dados = [df_cont_fem.iloc[0], df_cont_masc.iloc[0]]

st.text(f"Homens: {dados[1]}, Mulheres {dados[0]}")