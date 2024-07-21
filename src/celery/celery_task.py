from celery import Celery
from config_celery import REDIS_HOST, REDIS_PORT, REDIS_USER, REDIS_USER_PASSWORD
import aioredis
import aioredis.client

import aiohttp
import xml.etree.ElementTree as ET
from asyncio import run


app = Celery('example', broker=f'redis://{REDIS_USER}:{REDIS_USER_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1')


async def connect_to_redis():
    return await aioredis.from_url(f'redis://{REDIS_USER}:{REDIS_USER_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0')


async def fetch_xml_data():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.cbr.ru/scripts/XML_daily.asp') as response:
            xml_data = await response.text()
            return xml_data


@app.task
async def update_currency_rates():
    xml_data = await fetch_xml_data()
    root = ET.fromstring(xml_data)
    
    r = await connect_to_redis()
    
    for valute in root.findall('Valute'):
        currency_code = valute.find('CharCode').text
        currency_rate = valute.find('Value').text.replace(',', '.')
        await r.set(currency_code, currency_rate)
    await r.close()


app.conf.CELERYBEAT_SCHEDULE = {
    'my-periodic-task': {
        'task': 'tasks.update_currency_rates',
        'schedule':5.0,  
    },
}



