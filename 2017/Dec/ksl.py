import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from re import sub
import smtplib
from email.mime.text import MIMEText

base_url = "https://www.ksl.com"
initial_url = "https://www.ksl.com/classifieds/s/Computers/Desktop+Hardware+and+Accessories"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

r = requests.get(initial_url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

listings = soup.select('div.listing')

def send_text(title, price, url):
    from config import sender, password
    # Define to/from
    casey = '8018217046@vtext.com'
    jarrod = '3854777637@msg.fi.google.com'

    # Create message
    msg = MIMEText("{}: {} - {}".format(title, price, url))
    msg['From'] = sender
    msg['To'] = 'KSL shoppers'

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operations via server
    server.login(sender, password)
    server.sendmail(sender, [casey, jarrod], msg.as_string())
    server.quit()

mapping = {
    "280": Decimal('150.00'),
    "380": Decimal('150.00'),
    "390": Decimal('200.00'),
    "480": Decimal('250.00'),
    "580": Decimal('250.00'),
    "470": Decimal('250.00'),
    "570": Decimal('250.00'),
    "1050": Decimal('150.00'),
    "1060": Decimal('250.00'),
    "1070": Decimal('375.00'),
    "1070 ti": Decimal('400.00'),
    "1080": Decimal('475.00'),
    "1080 ti": Decimal('650.00')
}

for listing in listings[1:]:
    title = " ".join(listing.select_one('h2').find("a").text.replace('\n','').split())
    price = Decimal(sub(r'[^\d.]', '', " ".join(listing.select_one('h3').text.replace('\n','').split())))
    href = listing.select_one('h2').find("a")['href']
    tos = listing.select_one('span.timeOnSite').text
    recent = False
    if 'Min' in tos:
        minutes = int(tos.split()[1])
        if minutes < 5:
            recent = True
    if not recent:
        continue
    for item, cost in mapping.items():
        if item in title and price <= cost:
            send_text(title, price, base_url+href)
