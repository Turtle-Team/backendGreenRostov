import sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
import importlib
import os


SQLALCHEMY_DATABASE_URL = os.getenv('BASE_URL')
# SQLALCHEMY_DATABASE_URL = "postgresql://user_name:password@localhost/postgres"

modules = os.listdir('database')

for module in modules:
    if os.path.isdir(os.path.join('database', module)):
        importlib.import_module(f'database.{module}')



class Database:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)

    def get_marker(self):
        return scoped_session(sqlalchemy.orm.sessionmaker(bind=self.engine))
