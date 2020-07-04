import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template,request
from flask import jsonify
from flask_cors import CORS, cross_origin
import urllib.request
import json,os
from re import sub
from decimal import Decimal

app = Flask(__name__)


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/",methods = ['POST', 'GET'])
@cross_origin()

def load_api():

	url_world = 'https://www.worldometers.info/coronavirus/'
	r_world = requests.get(url_world)
	s_world = BeautifulSoup(r_world.text, "html.parser")
	data_world = s_world.find_all("div", class_ = "maincounter-number")
	
	
	url_brazil = 'https://www.worldometers.info/coronavirus/country/brazil/'
	r_brazil = requests.get(url_brazil)
	s_brazil = BeautifulSoup(r_brazil.text, "html.parser")
	data_brazil = s_brazil.find_all("div", class_ = "maincounter-number")
	
	w0 = data_world[0].text.strip()
	#w0 = float(w0.replace(",","."))
	w0_ = Decimal(sub(r'[^\d.]', '', w0))
	
	
	w1 = data_world[1].text.strip()
	w1_ = Decimal(sub(r'[^\d.]', '', w1))
	#w1 = float(w1.replace(",","."))
	
	w2 = data_world[2].text.strip()
	#w2 = float(w2.replace(",","."))
	w2_ = Decimal(sub(r'[^\d.]', '', w2))
	
	b0 = data_brazil[0].text.strip()
	#b0 = float(b0.replace(",","."))
	b0_ = Decimal(sub(r'[^\d.]', '', b0))
	print(b0_)
	
	b1 = data_brazil[1].text.strip()
	#b1 = float(b1.replace(",","."))
	b1_ = Decimal(sub(r'[^\d.]', '', b1))
	
	b2 = data_brazil[2].text.strip()
	#b2 = float(b2.replace(",","."))
	b2_ = Decimal(sub(r'[^\d.]', '', b2))
	print(b2_)
	
	_calc = lambda x, y: round(((x * 100) / y), 2)
	
	world_death_rate = _calc(w1_, w2_)
	
	brazil_death_rate = _calc(b1_, b2_)
	
	world_recovered_rate = _calc(w2_, w0_)
	
	brazil_recovered_rate = _calc(b2_, b0_)
    
	
	
	
	world_data_set = {"COVID19Cases":
      w0, "Deaths": w1,
      "Recoveries": w2,
      "DeathRate": str(world_death_rate),
      "RecoveredRate": str(world_recovered_rate)}
       #"LastUpdated":world_lastupdated}
        
	brazil_data_set = {"COVID19Cases":
    	b0, "Deaths": b1,
    	"DeathRate": str(brazil_death_rate),
    	"Recoveries": b2,
    	"RecoveredRate": str(brazil_recovered_rate)}
    	
	corona_array = {
        "World": world_data_set,
        "Brazil": brazil_data_set
    }
    
	return jsonify(COVID19=corona_array)
	

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = float(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()
