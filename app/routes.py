from flask import render_template, url_for
from app.forms import WeatherForm
from app import app, db
from app.models import City
import requests



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WeatherForm()
    weather = {}
    if form.validate_on_submit():
        geocode_url = 'https://eu1.locationiq.com/v1/search.php?'
        geocode_data = {
                'key': 'pk.c8453946375eb2d3d309f14ea69695ee',
                'q': form.city.data,
                'format': 'json'
                }
        geocode_res = requests.get(geocode_url, params=geocode_data).json()
        lat = geocode_res[0]['lat']
        lon = geocode_res[0]['lon']

        url = 'https://api.darksky.net/forecast/b138661417c97e3b128276fe4fcbf795'
        data = '/{},{}?exclude=minutely,hourly,daily,flags&units=auto'
        r = requests.get(url + data.format(lat, lon)).json()

        weather = {
                'city': form.city.data,
                'temp': r['currently']['temperature'],
                'summary': r['currently']['summary'],
                }
    return render_template('index.html', title='Home',
            form=form, weather=weather)


