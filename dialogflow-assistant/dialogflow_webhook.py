from flask import Flask, request, jsonify
import requests
from dialogflow_webhook_response import *


app = Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return jsonify({"status":"ok"})

@app.route('/',methods=['GET','POST'])
def index():
    with open("./credentials.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        key = cfg['credentials']['GOOGLE_KEY']

    req = request.get_json()
    session = req.get('session') #get session id
    query = req.get('queryResult').get('parameters').get('query') #retrieve the value of the entity query
    radius = req.get('queryResult').get('parameters').get('number') # retrieve the value of the entity radius

    get_origin = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(api_key)).json() # get user's current location
    origin_lat = get_origin['location']['lat']
    origin_lng = get_origin['location']['lng']

    place = requests.get(
        'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}'.format(
            origin_lat, origin_lng, radius, query, api_key)).json() # look for a places
    if len(place['results']) == 0:
        text = "Sorry, I didn't find anything"
        response = empty_response(text)
    else:
        for i in place['results']:
            if 'rating' and 'vicinity' in i.keys():
                name = i['name']
                rating = i['rating']
                address = i['vicinity']
                if i['opening_hours']['open_now']==True:
                    opening_hours = 'open'
                else:
                    opening_hours = 'closed'
                break
        text = "I found a {} called {} based on your search parameters.".format(query, name)
        response = place_response(text, session, address, opening_hours, rating)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)




