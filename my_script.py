
import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv("Advertising_F.csv")
st.title("Advertising Dashboard by City Michael Frasketi")

st.sidebar.head("Filters")
x_var=st.selectbox("X axis",["TV","raido","newspaper"])

#show scatter plot
px.scatter(df,x='TV',y='radio',
           labels={'TV': 'Tv add spend','radio':'Radio add spend'})

st.plotly_chart(fig)

#show the barplot
sales_per_city=df.groupby("City")["sales"].sum().reset.index()
fig=px.bar(sales_per_city,x='City',y='sales',title="data is fun")
st.plotly_chart(fig)

st.datafrom(df)
