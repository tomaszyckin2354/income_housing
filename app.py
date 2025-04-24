import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/main/CT-affordable-housing-2011-2022.csv')
df1 = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/main/CT-towns-income-census-2020.csv')

st.title('Affordable Housing in Hartford Compared to Connectict Nolan Tomaszycki & Estela Baka')

# Filter to just 2011 and 2020
df_filtered = df[df['Year'].isin([2011, 2020])]

# Pivot to get towns as rows, years as columns
df_pivot = df_filtered.pivot(index='Town', columns='Year', values='Percent Affordable')

# Drop towns missing either year
df_pivot = df_pivot.dropna()

# Calculate change from 2011 to 2020
df_pivot['Change'] = df_pivot[2020] - df_pivot[2011]

# Sort towns by change
df_sorted = df_pivot.sort_values(by='Change')

# Set color: red for negative, green for positive
colors = df_sorted['Change'].apply(lambda x: 'red' if x < 0 else 'green')

# Plot
fig, ax = plt.subplots(figsize=(8, 10))
ax.barh(df_sorted.index, df_sorted['Change'], color=colors)
ax.set_xlabel("Percentage Change in Affordability")
ax.set_ylabel("Towns")
ax.set_title("Towns with Largest Increase/Decrease in Housing Affordability (2011-2020)")
plt.tight_layout()

# Show in Streamlit
st.pyplot(fig)
