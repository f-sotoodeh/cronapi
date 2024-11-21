import os

from pymongo import MongoClient

MONGO_URI = 'mongodb://root:ea02910866ed4c0f9a982a489f606b76@mongo_db:27017/cronapi?authSource=admin'
DB_NAME = MONGO_URI.split('/')[-1].split('?')[0]
DB = MongoClient().get_database(DB_NAME)
