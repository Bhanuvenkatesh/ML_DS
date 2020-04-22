import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response


app=Flask(_name_)

@app.route('/webhook', methods=['POST'])

defwebhook():

	req=request.get_json(silent=True, force=True)

	print(json.dumps(req,indent =4))

	res=makeResponse(req)
	res=json.dumps(res, indent=4)
	r=make_response(res)
	r.headers['Content-Type']='application/json'
	return r
	
defmakeResponse(req):
	
	result=req.get("queryResult")
	parameters=result.get("parameters")
	city=parameters.get("geo-city")
	date=parameters.get("date")
	
r=requests.get('http://api.openweathermap.org/data/2.5/forecast?q=hyderabad,in&appid=db91df44baf43361cbf73026ce5156cb')
	json_object=r.json()
	weather=json_object['list']
	condition=weather[0]['weather'][0]['description']
	speech="The forecast for "+city+ " for "+date+" is "+ condition
	return{
		"fulfillmentMessages": [
		{
			"text": {
				"text": speech
			}
		}]}
	
if__name__=='__main__':

	port=int(os.getenv('PORT',5000))
	print("starting on port %d"% port)
	app.run(debug=False, port=port, host='0.0.0.0')
