from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any

from beanie import Document


class Response_Model(BaseModel):
    success: bool
    message: Optional[str]
    data: Optional[Any]

    class Config:
        json_schema_extra = {
            'success': True,
            'message': '',
            'data': None,
        }


class Test(Document):
    text: str
    datetime: datetime


