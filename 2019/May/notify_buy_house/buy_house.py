import requests
import json
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from os import listdir
from os.path import isfile, join

from utils import send_text

send_to_list = ["8018217046@msg.fi.google.com", "8643809345@vtext.com"]
zips = [84043, 84003, 84004, 84020, 84065, 84096]
ogden_zips = [84403, 84404, 84405, 84067, 84414, 84401]
clev = 44116
today = datetime.now()
list_time_delta = timedelta(hours=32)
prop_types = ['single_family', 'condo']


def get_property_in_zip(zip_code):
    initial_url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties?postal_code={}&client_id=rdc_mobile_native&limit=200'.format(
        zip_code)
    properties = requests.get(initial_url).json().get("properties")
    return properties


def get_property_info(listing_id):
    listing_url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties/{0}?client_id=rdc_mobile_native'.format(listing_id)
    listing = requests.get(listing_url).json()
    return listing


def get_datetime_from_list_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    except:
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.000Z")


def check_property_info(property_info, exclude_ids):
    list_date = get_datetime_from_list_date(property_info.get("list_date"))
    property_id = property_info.get("listing_id")
    beds = property_info.get("beds")
    baths_full = property_info.get("baths_full")
    year_built = property_info.get("year_built")
    price = property_info.get("price")
    prop_type = property_info.get("prop_type")
    if not property_id or not beds or not list_date or not baths_full or not year_built or not price or not prop_type:
        return False
    if (beds >= 3 and baths_full >= 2 and year_built > 1900 and 400000 >= price >= 150000 and prop_type in prop_types
            and today - list_date < list_time_delta and property_id not in exclude_ids):
        with open(f'data/{property_info.get("listing_id")}.json', 'a') as f:
            f.write(json.dumps(property_info) + "\n")
        send_text(property_info.get("rdc_web_url"), send_to_list)
        return True
    else:
        return False


def get_ids_already_sent(path):
    return [f[:-5] for f in listdir(path) if isfile(join(path, f))]


def evaluate_and_send_texts_for_zips(zips, exclude_ids):
    for zip_code in zips:
        properties = get_property_in_zip(zip_code)
        with ThreadPoolExecutor(max_workers=30) as executor:
            try:
                results = list(executor.map(check_property_info, properties, repeat(exclude_ids)))
            except:
                print(f"{zip_code} problem")


if __name__ == "__main__":
    already_sent_ids = get_ids_already_sent('data/')
    evaluate_and_send_texts_for_zips(ogden_zips, already_sent_ids)
