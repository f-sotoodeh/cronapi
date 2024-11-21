from datetime import datetime
from os import getenv

from database import DB

def test():
    DB['Test'].insert_one(dict(
        datetime=datetime.now(),
        text='test',
    ))


if __name__ == '__main__':
    print('CRON ~~~~~~~~~~ TEST')
    test()
