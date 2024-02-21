import streamlit as st
import plotly.express as px
from backend import get_data
place = st.text_input("Place: ")
st.title("Weather Forecast for the Next Days")

days = st.slider("Forest Days:", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
if place:
    try:


        filtered_data, t = get_data(place, days, option)
        print((filtered_data))
        # d, t = get_data(days)
        if option == "Temperature":
            figure = px.line(x =t, y=filtered_data, labels={"x": "Date", "y": "Tempertature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in filtered_data]
            st.image(image_paths,caption=t, width=115)
    except KeyError:
        st.write("Địa chỉ không hợp lệ")