import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import seaborn as sns
sns.set(color_codes=True)
from Timeseries import timeSeries
from dataCleaner import cleaner
from windrosePlot import plotWindrose   

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Solar radiation analysis",page_icon=":chart_with_upwards_trend:", layout="wide")

st.title(" :chart_with_upwards_trend: Solar Radiation EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

region_list = ["benin-malanville","sierraleone-bumbuna","togo-dapaong_qc"]

st.sidebar.header("Pick your Region: ")
region = st.sidebar.selectbox("select",region_list)
region = "benin-malanville"
df = pd.read_csv("../../data/"+ region + ".csv", encoding = "ISO-8859-1")

col1, col2 = st.columns((2))

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

startDate = pd.to_datetime(df["Timestamp"]).min()
endDate = pd.to_datetime(df["Timestamp"]).max()

with col1:
    date1  = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2  = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Timestamp"] >= date1) & (df["Timestamp"] <= date2)].copy()

df_corrected = cleaner(df)

stat_summary = df_corrected.describe(percentiles=[0.5])

with col1:
    st.subheader("Statistical Summary")

st.table(stat_summary)

st.subheader("Time series analysis")
with st.expander("Expand for timeseries charts"):
    ghi_monthly_data = timeSeries(df_corrected,"GHI")

    ghi_fig = px.line(ghi_monthly_data, x=ghi_monthly_data.index, y=ghi_monthly_data['GHI'])
    st.caption('GHI recording from 2021 - 2022')
    st.plotly_chart(ghi_fig,use_container_width=True,height =20)

    dni_monthly_data = timeSeries(df_corrected,"DNI")

    dni_fig = px.line(dni_monthly_data, x=dni_monthly_data.index, y=dni_monthly_data['DNI'])
    st.caption('DNI recording from 2021 - 2022')
    st.plotly_chart(dni_fig,use_container_width=True,height =20)

    dhi_monthly_data = timeSeries(df_corrected,"DHI")

    dhi_fig = px.line(dhi_monthly_data, x=dhi_monthly_data.index, y=dhi_monthly_data['DHI'])
    st.caption('DHI recording from 2021 - 2022')
    st.plotly_chart(dhi_fig,use_container_width=True,height =20)

    tamb_monthly_data = timeSeries(df_corrected,"Tamb")

    tamb_fig = px.line(tamb_monthly_data, x=tamb_monthly_data.index, y=tamb_monthly_data['Tamb'])
    st.caption('Ambient temperature recording from 2021 - 2022')
    st.plotly_chart(tamb_fig,use_container_width=True,height =20)

    df_extracted = df_corrected.loc[:,['GHI','DNI','DHI','TModA','TModB']]

st.subheader("Correlation analysis")
with st.expander("Expand to see correlations"):
    st.table(df_extracted.corr())
 

st.subheader("Histogram")
with st.expander("Expand for histogram charts"):
    df_histo = df_corrected.loc[:, ['GHI', 'DNI', 'DHI', 'WS', 'Tamb','TModA','TModB']]

    histo_fig = px.bar(df_histo.mean(),title="Frequency distribution of certain variables")
    st.plotly_chart(histo_fig,use_container_width=True,height =20)

st.subheader("Boxplots")
with st.expander("Expand for boxplot charts"):
    bx1 = px.box(df['GHI'])
    st.plotly_chart(bx1,use_container_width=True,height =20)

    bx2 = px.box(df['DNI'])
    st.plotly_chart(bx2,use_container_width=True,height =20)

    bx3 = px.box(df['DHI'])
    st.plotly_chart(bx3,use_container_width=True,height =20)

    bx4 = px.box(df['Tamb'])
    st.plotly_chart(bx4,use_container_width=True,height =20)

    bx5 = px.box(df['TModA'])
    st.plotly_chart(bx5,use_container_width=True,height =20)

    bx6 = px.box(df['TModB'])
    st.plotly_chart(bx6,use_container_width=True,height =20)
