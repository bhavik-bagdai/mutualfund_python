import os

from sqlalchemy import create_engine, MetaData, result_tuple
from databases import Database
from sqlalchemy.testing.config import db_url
import os
from sqlalchemy.testing.suite.test_reflection import metadata

db_url = "mysql+mysqlconnector://root@localhost:3306/mfdb"

# db_url = os.getenv("Db_url")
if not db_url:
    raise ValueError("Environment variable not set")


engine = create_engine(db_url)
metadata = MetaData()
database = Database(db_url)