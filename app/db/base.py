from sqlalchemy.orm import declarative_base

from .session import engine
from .models.address import Address

Base = declarative_base()


# Import all models here for Alembic
def init_db():
    Base.metadata.create_all(bind=engine)
