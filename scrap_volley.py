# -*- coding: utf-8 -*-
"""Scrap Volley.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10WkfYy0x3EnGDnpxrwDs7B6UEi1qAu00
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/statistics/women/best-setters/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

levantadoras = []

for row in soup.find_all ('tr',attrs={'class': 'vbw-o-table__row'}):
    colunas = row.find_all("td")
    nome = colunas[1].text
    pais = colunas[2].text
    success = int(colunas[3].text)
    attempts = int(colunas[4].text)
    levantadoras.append({'Nome': nome, 'Pais': pais, 'success': success,
                         'attempts': attempts })

df = pd.DataFrame(levantadoras)
df.to_csv('levantadoras_vnl.csv', index=False)

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = 'levantadoras_vnl.csv'

if not os.path.exists(file_path):
    print(f"File {file_path} not found!")
else:
    df = pd.read_csv(file_path)

    top_10 = df.nlargest(20, 'success')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_10, x='success', y='Nome', palette='viridis')
    plt.title('Top 10 Levantadoras da VNL')
    plt.xlabel('Estatística')
    plt.ylabel('Nome')
    plt.show()

import streamlit as st
import pandas as pd

df = pd.read_csv('levantadoras_vnl.csv')
top_10 = df.nlargest(10, 'success')['Nome'].tolist()

st.title('Desafio: Adivinhe as Top 10 Levantadoras da VNL')

user_input = st.text_input('Digite o nome de uma jogadora:')

if user_input:
    if user_input in top_10:
        st.success(f'{user_input} está no top 10!')
    else:
        st.error(f'{user_input} não está no top 10. Tente novamente!')

if st.button('Mostrar Top 10'):
    top_10_grafico = df.nlargest(10, 'success')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_10_grafico, x='success', y='Nome', palette='viridis')
    plt.title('Top 10 Levantadoras da VNL')
    plt.xlabel('Estatísticas')
    plt.ylabel('Nome')
    st.pyplot(plt)