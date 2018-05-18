import geocoder
import json
import base64
import zlib
from difflib import SequenceMatcher
import csv
import requests

#create a set of longitudes and latitudes
class location:
    distance = ""
    accuracy = ""
    google_address = ""
    osm_address = ""
    mapzen_address = ""
    def __init__(self, lat, lon):
        self.longitude = lon
        self.latitude = lat

    def __str__(self):
        return "[" + self.longitude + ", " + self.latitude + "]"

locations = set()

#read in the Huge json file (probably best little by little)
with open('../data/gpspoints.json') as d:
    data = json.load(d)

###clean and decode the data
###for each gps points
small = 0
for points in data["RECORDS"]:
    p = points["GpsPoints"]
    #Base64 decode the gps points
    tmp = base64.b64decode(p)
    #unGzip the points
    try:
        ddata = zlib.decompress(tmp, 16 + zlib.MAX_WBITS).decode("utf-8")
    except:
        continue
    #get the longitudes and latitudes
    ll = []
    for point in ddata.split('|'):
        if not point:
            continue
        ll.append([point.split(",")[0],point.split(",")[1]])
    #add the first and last location in the gpspoints (start and end destinations)
    locations.add(location(ll[0][0],ll[0][1]))
    locations.add(location(ll[-1][0], ll[-1][1]))
    if small > 30:
        break
    small += 1

def osm_address(address):
    response = ""
    try:
        if address.get('house_number'):
            response += address['house_number'] + " "
        response += address['road'] + ", "
        if address.get('city'):
            response += address['city']
        elif address.get('town'):
            response += address['town']
        elif address.get('hamlet'):
            response += address['hamlet']
        else:
            response += address['county']
        response += ", " + address['state'] + " "
        if address.get('postcode'):
            response += address['postcode']
        if address['country'] == 'United States of America':
            response += ", USA"
        else:
            response += ", " + address['country']
        return response
    except:
        print(address)
    try:
        if address.get('county'):
            response += address['county'] + ", " 
        response += address['state'] + ", "
        if address['country'] == 'United States of America':
            response += ", USA"
        else:
            response += ", " + address['country']
        return response
    except:
        return ""

with open('test.csv', 'w') as output:
    writer = csv.writer(output, delimiter=',')
    for location in locations:

        google = geocoder.google([float(location.latitude),float(location.longitude)], method='reverse')
        osm = requests.get('https://maps.mauza.net/nominatim/reverse?lat=' + location.latitude + '&lon=' + location.longitude + '&format=json').json()
        location.google_address = google.address
        location.osm_address = osm_address(osm['address'])
        accuracy = SequenceMatcher(None, location.google_address, location.osm_address).ratio()
        accuracy2 = SequenceMatcher(None, location.google_address, osm['display_name']).ratio()
        writer.writerow([location.google_address, location.osm_address, accuracy, " ", osm['display_name'], accuracy2])


#store each address attached


#compare the location from each provider


