import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print(f"Weather in {city}: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or API key is invalid.")

if __name__ == "__main__":
    api_key = "https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${APIkey}"
    city = input("Enter city name: ")
    get_weather(api_key, city)
