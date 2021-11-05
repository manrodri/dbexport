import os
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# export DB_URL=postgresql://admin:password@$PUBLIC_IP:80/reviews

@lru_cache(maxsize=32)
def engine(db_url=None):
    db_url = db_url or os.getenv('DB_URL')
    if not db_url:
        raise ValueError('database URL is required')
    return create_engine(db_url)


def get_connection(db_url=None):
    return engine(db_url).connect()


@lru_cache()
def session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))

try:
    Session = session_class()
except:
    pass