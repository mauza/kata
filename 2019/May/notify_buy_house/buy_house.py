import requests
import time
import json
from datetime import datetime, timedelta

from utils import send_text

send_to_list = ["8018217046@msg.fi.google.com"]
zips = [84043, 84003, 84004, 84020, 84065, 84096]
clev = 44102
today = datetime.now()
list_time_delta = timedelta(hours=1)

def get_property_in_zip(zip_code):
    initial_url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties?postal_code={}&client_id=rdc_mobile_native&limit=200'.format(zip_code)
    properties = requests.get(initial_url).json().get("properties")
    return properties

def get_property_info(listing_id):
    listing_url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties/{0}?client_id=rdc_mobile_native'.format(listing_id)
    listing = requests.get(listing_url).json()
    return listing

def check_property_info(property_info):
    property_listing_delta = today - datetime.strptime(property_info.get("list_date"),"%Y-%m-%dT%H:%M:%SZ")
    if ( property_info.get("beds") and
         property_info.get("baths_full") and
         property_info.get("year_built") and
         property_info.get("price") and
         property_info.get("baths_full") and
         property_info.get("beds") >=4 and
         property_info.get("baths_full") >=2 and
         property_info.get("year_built") >=1990 and
         property_info.get("price") <=400000 and
         property_info.get("prop_type") == "single_family" and
         property_listing_delta < list_time_delta):
        return True
    else:
        return False

def main():
    for zip_code in zips:
        properties = get_property_in_zip(zip_code)
        for property in properties:
            if check_property_info(property):
                with open('data/houses.json', 'a') as f:
                    f.write(json.dumps(property) + "\n")
                send_text(property.get("rdc_web_url"), send_to_list)

if __name__ == "__main__":
    props = get_property_in_zip(clev)
    for p in props:
        if p.get('prop_type') == "multi_family":
            print(p)
