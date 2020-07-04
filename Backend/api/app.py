import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template,request
from flask import jsonify
from flask_cors import CORS, cross_origin
import urllib.request
import json,os
from re import sub
from decimal import Decimal
import re

app = Flask(__name__)


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/",methods = ['POST', 'GET'])
@cross_origin()

def load_api():

	url_world = 'https://www.worldometers.info/coronavirus/'
	r_world = requests.get(url_world)
	s_world = BeautifulSoup(r_world.text, "html.parser")

	last_update = s_world.find(text=re.compile('Last updated:'))

	data_world = s_world.find_all("div", class_ = "maincounter-number")
	data_table_world = s_world.find_all("div", class_ = "number-table-main")
	data_number_table_world = s_world.find_all("span", class_ = "number-table")
	
	
	url_brazil = 'https://www.worldometers.info/coronavirus/country/brazil/'
	r_brazil = requests.get(url_brazil)
	s_brazil = BeautifulSoup(r_brazil.text, "html.parser")
	data_brazil = s_brazil.find_all("div", class_ = "maincounter-number")
	data_table_brazil = s_brazil.find_all("div", class_ = "number-table-main")
	data_number_table_brazil = s_brazil.find_all("span", class_ = "number-table")
	
	wnt0 = data_number_table_world[0].text.strip()
	wnt0_ = Decimal(sub(r'[^\d.]', '', wnt0))

	wnt1 = data_number_table_world[1].text.strip()
	wnt1_ = Decimal(sub(r'[^\d.]', '', wnt1))

	bnt0 = data_number_table_brazil[0].text.strip()
	bnt0_ = Decimal(sub(r'[^\d.]', '', bnt0))

	bnt1 = data_number_table_brazil[1].text.strip()
	bnt1_ = Decimal(sub(r'[^\d.]', '', bnt1))
	

	wt0 = data_table_world[0].text.strip()
	wt0_ = Decimal(sub(r'[^\d.]', '', wt0))

	bt0 = data_table_brazil[0].text.strip()
	bt0_ = Decimal(sub(r'[^\d.]', '', bt0))

	wt1 = data_table_world[1].text.strip()
	wt1_ = Decimal(sub(r'[^\d.]', '', wt1))

	bt1 = data_table_brazil[1].text.strip()
	bt1_ = Decimal(sub(r'[^\d.]', '', bt1))
	

	w0 = data_world[0].text.strip()
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
	#print(b0_)
	
	b1 = data_brazil[1].text.strip()
	#b1 = float(b1.replace(",","."))
	b1_ = Decimal(sub(r'[^\d.]', '', b1))
	
	b2 = data_brazil[2].text.strip()
	#b2 = float(b2.replace(",","."))
	b2_ = Decimal(sub(r'[^\d.]', '', b2))
	#print(b2_)
	
	_calc = lambda x, y: round(((x * 100) / y), 2)
	
	world_death_rate = _calc(w1_, wt1_)

	world_condition_rate = _calc(wnt0_, wt0_)

	world_critical_rate = _calc(wnt1_, wt0_)

	brazil_condition_rate = _calc(bnt0_, bt0_)

	brazil_critical_rate = _calc(bnt1_, bt0_)
	
	brazil_death_rate = _calc(b1_, bt1_)
	
	world_recovered_rate = _calc(w2_, wt1_)
	
	brazil_recovered_rate = _calc(b2_, bt1_)
    
	
	
	
	world_data_set = {"COVID19Cases":
      w0, "Deaths": w1,
      "Recoveries": w2,
	  "ActiveCases": wt0,
	  "MildCondition": wnt0,
	  "SeriousOrCritical": wnt1,
	  "ClosedCases": wt1,
      "DeathRate": str(world_death_rate),
	  "ConditionRate": str(world_condition_rate),
	  "CriticalRate": str(world_critical_rate),
      "RecoveredRate": str(world_recovered_rate)}
       #"LastUpdated":world_lastupdated}
        
	brazil_data_set = {"COVID19Cases":
    	b0, "Deaths": b1,
    	"DeathRate": str(brazil_death_rate),
    	"Recoveries": b2,
		"ActiveCases": bt0,
	  	"MildCondition": bnt0,
	  	"SeriousOrCritical": bnt0,
		"ConditionRate": str(brazil_condition_rate),
	  	"CriticalRate": str(brazil_critical_rate),
	  	"ClosedCases": bt1,
    	"RecoveredRate": str(brazil_recovered_rate)}

	update_data_set = {"LastUpdate":
    	last_update
	}
    	
	corona_array = {
        "World": world_data_set,
        "Brazil": brazil_data_set,
		"Update": update_data_set
    }
    
	return jsonify(COVID19=corona_array)
	

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = float(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()
