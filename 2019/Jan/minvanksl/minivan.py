import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
from re import sub
import smtplib
from email.mime.text import MIMEText

base_url = "https://www.ksl.com"
url = "https://www.ksl.com/auto/search/index?yearFrom=2009&mileageTo=135000&priceTo=9500&sellerType%5B%5D=For+Sale+By+Owner&titleType%5B%5D=Clean+Title&body%5B%5D=Minivan"

def send_text(title, price, url):
    from config import sender, password
    # Define to/from
    Lori = '8013108931@vtext.com'
    Casey = '8018217046@tmomail.net'

    # Create message
    msg = MIMEText("{}: {} - {}".format(title, price, url))
    msg['From'] = sender
    msg['To'] = 'KSL shoppers'

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operations via server
    server.login(sender, password)
    server.sendmail(sender, [Casey, Lori], msg.as_string())
    server.quit()

async def main():
    browser = await launch({'headless': True}, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(url)
    html = await page.content()
    await browser.close()
    return html

html = asyncio.get_event_loop().run_until_complete(main())

soup = BeautifulSoup(html, "html.parser")

listings = soup.select('div.listing')


for listing in listings:
    title = " ".join(listing.select('div')[1].find("a").text.replace('\n','').split())
    price = sub(r'[^\d.]', '', " ".join(listing.select('div')[2].text.replace('\n','').split()))
    href = listing.select('div')[1].find("a")['href']
    tos = " ".join(listing.select('div')[4].text.replace('\n','').split()).split(";")[1]
    recent = False
    if 'Min' in tos:
        minutes = int(tos.split()[0])
        if minutes < 32:
            recent = True
    if not recent:
        continue
    print(title)
    print(price)
    print(tos)
    print(href)
    send_text(title, price, base_url+href)