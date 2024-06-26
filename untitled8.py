# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wwFW10gAd-TktzcXXRjVFVpF14A3TfYT
"""

pip install streamlit

import streamlit as st

jogadoras = [
    {
        "nome": "Diao L.Y.",
        "pais": "China",
        "foto": "/content/diao linyu.jpg",
        "caracteristicas": "Diao Linyu is a Chinese indoor volleyball player. She is a member of China women's national volleyball team. She participated at the 2017 Volleyball World Grand Prix, 2018 Montreux Volley Masters, 2019 Montreux Volley Masters, and 2018 Asian Games. On club level, she plays for Jiangsu Zenith Steel.."
    },
    {
        "nome": "Brie",
        "pais": "Canada",
        "foto": "/content/brie.jpg",
        "caracteristicas": "Brie Joy O'Reilly é uma jogadora e musicista canadense de vôlei. Ela faz parte da seleção canadense de vôlei feminino. Profissionalmente, joga no clube brasileiro Sesc-RJ/Flamengo."
    },
    {
        "nome": "Dain",
        "pais": "Coreia",
        "foto": "/content/dain.jpg",
        "caracteristicas": "DAin is a Chinese indoor volleyball player. She is a member of Korea women's national volleyball team. She participated at the Korean V-League 2023/24, 2022/23,2017/18"
    },

]

st.title("Top 10 Levantadoras da VNL 2024")

for jogadora in jogadoras:
    st.header(jogadora["nome"])
    st.subheader(jogadora["pais"])
    st.image(jogadora["foto"], width=200)
    st.write(jogadora["caracteristicas"])
    st.write("---")