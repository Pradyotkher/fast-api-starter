from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
 
db_username = "fast-api-starter"
db_password = "dummyPassword"
db_name = "fastAPIDatabase"
SQL_ALCHEMY_DATABASE_URL = "mysql+pymysql://fast-api-starter:dummyPassword@localhost:3306/fastAPIDatabase"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL , echo=True)

base = declarative_base()

SessionLocal = sessionmaker(bind=engine , autoflush=False , autocommit = False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()