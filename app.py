import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/main/CT-affordable-housing-2011-2022.csv')
df1 = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/main/CT-towns-income-census-2020.csv')

st.title('Affordable Housing in Hartford Compared to Connectict Nolan Tomaszycki & Estela Baka')

df_filtered = df[df['Year'].isin([2011, 2020])]

df_pivot = df_filtered.pivot(index='Town', columns='Year', values='Percent Affordable')

df_pivot = df_pivot.dropna()

df_pivot['Change'] = df_pivot[2020] - df_pivot[2011]

df_sorted = df_pivot.sort_values(by='Change')

colors = df_sorted['Change'].apply(lambda x: 'red' if x < 0 else 'green')


fig, ax = plt.subplots(figsize=(8, 10))
ax.barh(df_sorted.index, df_sorted['Change'], color=colors)
ax.set_xlabel("Percentage Change in Affordability")
ax.set_ylabel("Towns")
ax.set_title("Towns with Largest Increase/Decrease in Housing Affordability (2011-2020)")
plt.tight_layout()

st.pyplot(fig)



cities = ['Waterbury', 'Stamford', 'Hartford', 'New Haven', 'Bridgeport']
years = [2014, 2018, 2022]

df_filtered = df[df['Town'].isin(cities) & df['Year'].isin(years)]


df_pivot = df_filtered.pivot(index='Town', columns='Year', values='Percent Affordable')


df_pivot = df_pivot.loc[cities]


fig, ax = plt.subplots(figsize=(8, 6))

bar_width = 0.25
x = range(len(df_pivot))


for i, year in enumerate(years):
    ax.bar([p + i*bar_width for p in x], df_pivot[year], width=bar_width, label=str(year))


ax.set_xticks([p + bar_width for p in x])
ax.set_xticklabels(df_pivot.index, rotation=45)
ax.set_ylabel("Housing Units")
ax.set_xlabel("Town")
ax.set_title("Percentage of Affordable Housing Units by City in 2014, 2018, and 2022")
ax.legend(title="Year")

plt.tight_layout()

# Show in Streamlit
st.pyplot(fig)



hartford = df[df['Town'] == 'Hartford'].sort_values('Year')


state_avg = df.groupby('Year')['Percent Affordable'].mean().reset_index()


fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(hartford['Year'], hartford['Percent Affordable'], color='red', label='Hartford')
ax.plot(state_avg['Year'], state_avg['Percent Affordable'], color='skyblue', label='State Average')


ax.set_title("Percentage of Affordable Housing by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Percent Affordable")
ax.set_ylim(0, 45)
ax.legend()


st.pyplot(fig)
