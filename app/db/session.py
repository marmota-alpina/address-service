from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import Config

engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
