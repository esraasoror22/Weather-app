from flask import Flask, render_template, request
import requests

app = Flask(__name__)
APIKEY = "54e31d4e1b7847cdb88164434251306"
BaseURL= "http://api.weatherapi.com/v1/current.json"

#https://www.weatherapi.com/api-explorer.aspx
#http://api.weatherapi.com/v1/current.json?key=54e31d4e1b7847cdb88164434251306&q=Egypt&aqi=no
@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        response = requests.get(f"{BaseURL}?key={APIKEY}&q={city}&aqi=no")
        if response.status_code == 200:
            weather_data = response.json()
            
        else:
            weather_data = {"error": "City not found!"}

    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 
    






