import os
from dotenv import load_dotenv



load_dotenv()


REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_USER = os.environ.get("REDIS_USER")
REDIS_USER_PASSWORD = os.environ.get("REDIS_USER_PASSWORD")
REDIS_PORT = os.environ.get("REDIS_PORT")

CELERY_TIME_UPDADE = os.environ.get("CELERY_TIME_UPDADE")