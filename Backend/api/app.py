from flask import Flask, render_template,request
from flask import jsonify
from flask_cors import CORS, cross_origin
import urllib.request
import json,os

app = Flask(__name__)


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/",methods = ['POST', 'GET'])
@cross_origin()

def load_api():
    link = "https://www.bing.com/covid/data"
    with urllib.request.urlopen(link) as response:
        json_data = response.read().decode("utf-8")
        _bingdata = json.loads(json_data)

    world_cases = _bingdata['totalConfirmed']
    world_deaths = _bingdata['totalDeaths']
    world_recovered = _bingdata['totalRecovered']
    world_lastupdated= _bingdata['lastUpdated']
    #print(world_lastupdated)

    # find brazil
    for index, j in enumerate(_bingdata['areas']):
        # [TODO] change 'brazil' for your country
        if j['id'] == 'brazil':
  
            brazil_cases = _bingdata['areas'][index]['totalConfirmed']
            brazil_deaths = _bingdata['areas'][index]['totalDeaths']
            brazil_recovered = _bingdata['areas'][index]['totalRecovered']
            
            bahia_cases = _bingdata['areas'][index]['areas'][8]['totalConfirmed']
           # print(bahia_cases)
            bahia_deaths = _bingdata['areas'][index]['areas'][8]['totalDeaths']
            #print(bahia_deaths)
            bahia_recovered = _bingdata['areas'][index]['areas'][8]['totalRecovered']
            ##################
            pernambuco_cases = _bingdata['areas'][index]['areas'][12]['totalConfirmed']
            #print(pernambuco_cases)
            pernambuco_deaths = _bingdata['areas'][index]['areas'][12]['totalDeaths']
            #print(bahia_deaths)
            pernambuco_recovered = _bingdata['areas'][index]['areas'][12]['totalRecovered']
           # print(bahia_recovered)
##################
            saopaulo_cases = _bingdata['areas'][index]['areas'][19]['totalConfirmed']
            #print(saopaulo_cases)
            saopaulo_deaths = _bingdata['areas'][index]['areas'][19]['totalDeaths']
            #print(bahia_deaths)
            saopaulo_recovered = _bingdata['areas'][index]['areas'][19]['totalRecovered']
           # print(bahia_recovered)
##################
            riodejaneiro_cases = _bingdata['areas'][index]['areas'][18]['totalConfirmed']
            #print(saopaulo_cases)
            riodejaneiro_deaths = _bingdata['areas'][index]['areas'][18]['totalDeaths']
            #print(bahia_deaths)
            riodejaneiro_recovered = _bingdata['areas'][index]['areas'][18]['totalRecovered']
           # print(bahia_recovered)
            
            break
            
    
    # [TODO] Rating Elements
    _calc = lambda x, y: round(((x * 100) / y), 2)
    
    	
    		
    world_death_rate = _calc(world_deaths, world_cases)
    brazil_death_rate = _calc(brazil_deaths, brazil_cases)
    if bahia_deaths is None:
    	bahia_death_rate = '-'
    	bahia_deaths = '-'
    else:
    	bahia_death_rate = _calc(bahia_deaths, bahia_cases)
    #########
    if pernambuco_deaths is None:
    	pernambuco_death_rate = '-'
    	pernambuco_deaths = '-'
    else:
    	pernambuco_death_rate = _calc(pernambuco_deaths, pernambuco_cases)

    if saopaulo_deaths is None:
    	saopaulo_death_rate = '-'
    	saopaulo_deaths = '-'
    else:
    	saopaulo_death_rate = _calc(saopaulo_deaths, saopaulo_cases)    

    if riodejaneiro_deaths is None:
    	riodejaneiro_death_rate = '-'
    	riodejaneiro_deaths = '-'
    else:
    	riodejaneiro_death_rate = _calc(riodejaneiro_deaths, riodejaneiro_cases)

    world_recovered_rate = _calc(world_recovered, world_cases)
    brazil_recovered_rate = _calc(brazil_recovered, brazil_cases)
    
    
    if bahia_recovered is None:
    	bahia_recovered_rate = '-'
    	bahia_recovered = '-'
    else:
    	bahia_recovered_rate = _calc2(bahia_recovered, bahia_cases)
    
	######   
    if pernambuco_recovered is None:
    	pernambuco_recovered_rate = '-'
    	pernambuco_recovered = '-'
    else:
    	pernambuco_recovered_rate = _calc2(pernambuco_recovered, pernambuco_cases) 
    	
    if saopaulo_recovered is None:
    	saopaulo_recovered_rate = '-'
    	saopaulo_recovered = '-'
    else:
    	saopaulo_recovered_rate = _calc2(saopaulo_recovered, saopaulo_cases)
    	
    if riodejaneiro_recovered is None:
    	riodejaneiro_recovered_rate = '-'
    	riodejaneiro_recovered = '-'
    else:
    	riodejaneiro_recovered_rate = _calc2(riodejaneiro_recovered, riodejaneiro_cases)  
    			    			
    world_data_set = {"COVID19Cases": world_cases, "Deaths": world_deaths, "DeathRate": world_death_rate,
                      "Recoveries": world_recovered, "RecoveredRate": world_recovered_rate, "LastUpdated":world_lastupdated}
    
    brazil_data_set = {"COVID19Cases":
    	brazil_cases, "Deaths": brazil_deaths,
    	"DeathRate": brazil_death_rate,
    	"Recoveries": brazil_recovered,
    	"RecoveredRate": brazil_recovered_rate}
    bahia_data_set = {"COVID19Cases":
    	bahia_cases, "Deaths": bahia_deaths,
    	"DeathRate": bahia_death_rate,
    	"Recoveries": bahia_recovered,
    	"RecoveredRate": bahia_recovered_rate}
    pernambuco_data_set = {"COVID19Cases":
    	pernambuco_cases, "Deaths":
    		pernambuco_deaths, "DeathRate":
    			pernambuco_death_rate,
    			"Recoveries": pernambuco_recovered,
    			"RecoveredRate":
    				pernambuco_recovered_rate}
    saopaulo_data_set = {"COVID19Cases":
		saopaulo_cases, "Deaths":
			saopaulo_deaths, "DeathRate":
				saopaulo_death_rate, "Recoveries":
					saopaulo_recovered,
					"RecoveredRate":
						saopaulo_recovered_rate}
    riodejaneiro_data_set = {"COVID19Cases":
		riodejaneiro_cases, "Deaths":
			riodejaneiro_deaths, "DeathRate":
				riodejaneiro_death_rate, "Recoveries":
					riodejaneiro_recovered,
					"RecoveredRate":
						riodejaneiro_recovered_rate}
    
    
    corona_array = {
        "World": world_data_set,
        "Brazil": brazil_data_set,
        "SaoPaulo": saopaulo_data_set,
        "RiodeJaneiro": riodejaneiro_data_set,
        "Bahia": bahia_data_set,
        "Pernambuco": pernambuco_data_set,      
    }
    
    return jsonify(COVID19=corona_array)
    #return render_template('index.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()
