import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


housing = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/main/CT-affordable-housing-2011-2022.csv')
income = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/main/CT-towns-income-census-2020.csv')

st.title('Affordable Housing in Hartford Compared to Connectict Nolan Tomaszycki & Estela Baka')
