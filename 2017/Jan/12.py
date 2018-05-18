import geocoder
import json
import base64
import zlib
from difflib import SequenceMatcher

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


tot_accuracy = 0
for location in locations:
    accuracy = 0
    #use geocoder and mapzen to get a reverse geocode.
    google = geocoder.google([float(location.latitude),float(location.longitude)], method='reverse')
    osm = geocoder.geocodefarm([float(location.latitude),float(location.longitude)], method='reverse')
    #farm = geocoder.geocodefarm([float(location.longitude),float(location.latitude)], method='reverse')
    location.google_address = google.address
    location.osm_address = osm.address
    if google.street and osm.street and SequenceMatcher(None, google.street, osm.street).ratio() > .6:
        accuracy += 1
    elif google.street and osm.street:
        print("google street: " + google.address)
        print("osm street: " + osm.address)
    else:
        print("street not there")
    if google.postal == osm.postal:
        accuracy += 1
    elif google.postal and osm.postal:
        print("google: " + google.postal)
        print("osm: " + osm.postal)
    else:
        print("postal not there")
    # if osm.confidence > google.confidence:
    #     accuracy += 1
    location.accuracy = accuracy
    tot_accuracy += accuracy

print("average total accuracy: " + str(tot_accuracy/len(locations)))

#store each address attached


#compare the location from each provider


