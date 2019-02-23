import asyncio

from pyppeteer import launch
from bs4 import BeautifulSoup
from re import sub

import requests

async def get_html(url):
    browser = await launch( 
        {'headless': False, 
        'executablePath': '/opt/google/chrome/chrome',
        'args': ['--user-data-dir=/home/mauza/.config/google-chrome']}
    )
    page = await browser.newPage()
    await page.goto(url, waitUntil='domcontentloaded')
    await page.waitFor('[data-action="getSummary"]', timeout=7000)
    pages = await page.querySelectorAll('[data-action="getSummary"]')
    #print(await pages[0].querySelectorEval('[data-action="getSummary"]', 'node => node.innerText'))
    await pages[0].click()
    await page.waitFor(7000)
    #await asyncio.gather(pages[0].click(), page.waitForNavigation(),)
    await browser.close()
    return pages


url = 'https://www.kaplanlearn.com/offline/qbank/23496054'
asyncio.get_event_loop().run_until_complete(get_html(url))
