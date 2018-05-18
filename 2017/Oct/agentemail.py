import requests
import csv
import time

zip_codes = []
with open('us_postal_codes.csv', 'r') as f:
    zip_code_file = csv.reader(f, delimiter=",")
    zip_code_file.__next__()
    for line in zip_code_file:
        zip_codes.append(line[0])

for zip_code in zip_codes:
    initial_url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties?postal_code={}&client_id=rdc_mobile_native&limit=200'.format(zip_code)
    time.sleep(0.5)
    properties = requests.get(initial_url).json()["properties"]
    print("Starting zip code: " + zip_code)
    for property in properties:
        print(property["address"]["city"])
        listing_id = property["listing_id"]
        listing_url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties/{0}?schema=legacy&listing_id={1}&client_id=rdc_mobile_native'.format(listing_id, listing_id)
        listing = requests.get(listing_url).json().get("listing")
        if not listing:
            continue
        agent = listing.get("agent")
        if agent:
            name = agent.get("name")
            email = agent.get("email")
            phone = agent.get("phone1")
            nra_id = agent.get("nrds_verified_id")
            office = agent.get("office_name")
            if phone:
                number = phone.get("number")
            else:
                number = None
            with open("output.csv", "a") as output:
                file = csv.writer(output, delimiter=",")
                file.writerow([name, email, number, nra_id, office, zip_code])

