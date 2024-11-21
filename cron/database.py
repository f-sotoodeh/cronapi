import os

from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = MONGO_URI.split('/')[-1].split('?')[0]
DB = MongoClient().get_database(DB_NAME)
