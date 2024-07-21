import aioredis as air

from config import *


async def connect_to_redis():
    return await air.from_url(f'redis://{REDIS_USER}:{REDIS_USER_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0')




