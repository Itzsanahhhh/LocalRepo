from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "b2692e1829e50dbd5554c90426c03e90"  # Get from OpenWeatherMap

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None

    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"]
            }
        else:
            weather = {"error": "City not found"}

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)