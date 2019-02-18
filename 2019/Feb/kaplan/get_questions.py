import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
from re import sub

import requests

async def get_html(url):
    browser = await launch({'headless': True, 'executablePath': '/usr/bin/chromium'}, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(url)
    html = await page.content()
    await browser.close()
    return html

url = 'https://www.kaplanlearn.com/education/test/getQuestion/23496054?testId=91015283&position=1'
html = asyncio.get_event_loop().run_until_complete(get_html(url))
print(html)