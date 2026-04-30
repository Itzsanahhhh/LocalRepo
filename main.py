import requests

API_KEY = "b2692e1829e50dbd5554c90426c03e90"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    print("\n--- Weather Report ---")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Condition:", desc)
else:
    print("City not found ❌")