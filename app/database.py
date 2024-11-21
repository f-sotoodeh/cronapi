from os import getenv

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket

from app.models import Test


MONGO_URI = 'mongodb://root:ea02910866ed4c0f9a982a489f606b76@mongo_db:27017/cronapi?authSource=admin'
MODELS = [Test]

# Initialize the database
async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.get_database()
    await init_beanie(database=db, document_models=MODELS)
