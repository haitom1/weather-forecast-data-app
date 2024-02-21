import requests

API_KEY = "b85b5aed7a0ab7a3f5520783d90b065e"
def get_data(place, forecast_days=None,kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filter_data[:nr_values]
    if kind == "Temperature":
        d = [dict["dt_txt"] for dict in filtered_data]
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]


    if kind == "Sky":
        d = [dict["dt_txt"] for dict in filtered_data]
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data, d

if __name__ == "__main__":
    print(get_data(place="Tokyo"))
