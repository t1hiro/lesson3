from flask import Flask

from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
	weather = weather_by_city('Moscow,Russia')
	if weather:
		return f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
	else:
		return 'Иноформация о погоде временно не доступна'

if __name__ == '__main__':
	app.run(debug=True)	