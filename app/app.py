from flask import Flask, render_template

from controls import Weather

app = Flask(__name__)


@app.route('/')
def get_weather():

    weather = Weather()

    result = weather.get()
    if result.get('error'):
        return result.get('error')

    context = dict(
        city_list=result.get('data')
    )

    return render_template('weather.html', **context)


if __name__ == '__main__':
    app.run(
        port=5000,
        host='0.0.0.0'
    )
