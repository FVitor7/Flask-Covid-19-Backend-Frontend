from flask import Flask
from flask import jsonify
import urllib.request
import json

app = Flask(__name__)


@app.route('/')
def load_api():
    link = "https://www.bing.com/covid/data"
    with urllib.request.urlopen(link) as response:
        json_data = response.read().decode("utf-8")
        _bingdata = json.loads(json_data)

    world_cases = _bingdata['totalConfirmed']
    world_deaths = _bingdata['totalDeaths']
    world_recovered = _bingdata['totalRecovered']

    # find brazil
    for index, j in enumerate(_bingdata['areas']):
        # [TODO] change 'brazil' for your country
        if j['id'] == 'brazil':
            brazil_cases = _bingdata['areas'][index]['totalConfirmed']
            brazil_deaths = _bingdata['areas'][index]['totalDeaths']
            brazil_recovered = _bingdata['areas'][index]['totalRecovered']
            break
    # [TODO] Rating Elements
    _calc = lambda x, y: round(((x * 100) / y), 2)
    world_death_rate = _calc(world_deaths, world_cases)
    brazil_death_rate = _calc(brazil_deaths, brazil_cases)
    world_recovered_rate = _calc(world_recovered, world_cases)
    brazil_recovered_rate = _calc(brazil_recovered, brazil_cases)

    world_data_set = {"COVID-19 Cases": world_cases, "Deaths": world_deaths, "Death Rate": world_death_rate,
                      "Recoveries": world_recovered, "Recovered Rate": world_recovered_rate}
    brazil_data_set = {"COVID-19 Cases": brazil_cases, "Deaths": brazil_deaths, "Death Rate": brazil_death_rate,
                       "Recoveries": brazil_recovered, "Recovered Rate": brazil_recovered_rate}

    corona_array = {
        "World": world_data_set,
        "Brazil": brazil_data_set
    }
    return jsonify(COVID19=corona_array)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run()
