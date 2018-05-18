import geocoder

lat = 40.7608
lon = -111.8910

location = geocoder.geocodefarm([lat,lon], key=None, method='reverse')

print(location.json)