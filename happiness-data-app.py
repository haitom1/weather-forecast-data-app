import streamlit as st
import plotly.express as px
import pandas as pd
st.title("In Search for Happiness")
option_x = st.selectbox("Select data for the X-asis",("happiness","gdp","generosity","corruption"))
option_y = st.selectbox("Select data for the Y-asis",("happiness","gdp","generosity","corruption"))

df = pd.read_csv("happy.csv")

x_array = None

match option_x:
    case "happiness":
        x_array = df["happiness"]
    case "gdp":
        x_array = df["gdp"]
    case "generosity":
        x_array = df["generosity"]
    case "corruption":
        x_array = df["corruption"]

y_array = None

match option_y:
    case "happiness":
        y_array = df["happiness"]
    case "gdp":
        y_array = df["gdp"]
    case "generosity":
        y_array = df["generosity"]
    case "corruption":
        y_array = df["corruption"]

st.subheader(f"{option_x} and {option_y}")
figure1 = px.scatter(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure1)