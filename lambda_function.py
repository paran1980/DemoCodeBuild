import json
import boto3
import requests

def lambda_handler(event,context):
    print(event)
    URL = "http://maps.googleapis.com/maps/api/geocode/json"
    location = event['landmark']
    PARAMS = {'address': location}
    print(PARAMS)
    print(location)
    r = requests.get(url= URL,
                     params = PARAMS)
    data = r.json()
    print(data)
    
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']
    
    print("Latitude:%s\nLongitude:%s\nFormattted Address:%s"
          %(latitude, longitude,formatted_address))
    output={"address":formatted_address}
    return output
