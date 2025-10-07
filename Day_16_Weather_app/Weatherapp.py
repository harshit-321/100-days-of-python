# Weather App using OpenWeatherMap API
# -------------------------------------

import requests

# Replace YOUR_API_KEY with your actual key from OpenWeatherMap
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

print("🌤️ Welcome to the Weather App 🌤️")
city = input("Enter city name: ")

# Create request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(url)
data = response.json()

# Check if the city is found
if data["cod"] == 200:
    main = data["main"]
    weather = data["weather"][0]
    temperature = main["temp"]
    humidity = main["humidity"]
    description = weather["description"].capitalize()

    print("\n📍 City:", city.title())
    print("🌡️ Temperature:", temperature, "°C")
    print("💧 Humidity:", humidity, "%")
    print("🌥️ Weather Condition:", description)
else:
    print("\n❌ City not found! Please enter a valid city name.")
