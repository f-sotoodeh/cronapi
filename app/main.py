from os import getenv, path
from datetime import datetime, timedelta
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from dotenv import load_dotenv
load_dotenv()

from app.database import init_db
from app.models import Response_Model, Test


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title='Cronapi',
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)



@app.get('/', response_model=Response_Model, tags=['Time'])
async def server_time(response: Response):
    """
    """
    try:
        data = dict(
            time=datetime.now().isoformat(),
            items=await Test.find().to_list(),
        )
        response.status_code = status.HTTP_200_OK
        return {
            'success': True,
            'message': 'Hey, we are up!',
            'data': data,
        }
    except Exception as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            'success': False,
            'message': str(e),
            'data': None,
        }



