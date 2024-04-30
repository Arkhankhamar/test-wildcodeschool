import streamlit as st
import pandas as pd

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)

df_weather

df_weather['DATE'] = pd.to_datetime(df_weather['DATE'])
df_weather.drop(['OPINION'], axis = 1, inplace=True)

st.line_chart(df_weather['MAX_TEMPERATURE_C'])

import seaborn as sns

viz_correlation = sns.heatmap(df_weather.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))

st.pyplot(viz_correlation.figure)