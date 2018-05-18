import json
import base64
import zlib
from gmplot import gmplot

with open('data/points_test.txt') as d:
    data = d.read()

tmp = base64.b64decode(data)

try:
    ddata = zlib.decompress(tmp, 16 + zlib.MAX_WBITS).decode("utf-8")
except:
    pass

points = [(float(p.split(',')[0]), float(p.split(',')[1])) for p in ddata.split('|') if p]
lats, lons = zip(*points)


gmap = gmplot.GoogleMapPlotter(float(points[0][0]), float(points[0][1]), 15)
gmap.plot(lats, lons, 'cornflowerblue', edge_width=10)
gmap.draw("my_map.html")