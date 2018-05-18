import geocoder

search = '1905 Spring Creek Drive Bountiful UT 84010'
loc = [40.8704889802915, -111.8683630197085]

g = geocoder.google(search)
print(g.json)

o = geocoder.osm(search)
print(o.json)

g = geocoder.google(loc, method="reverse")
print(g.json)

o = geocoder.osm(loc, method="reverse")
print(o.json)