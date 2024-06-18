import os


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/address_db')
