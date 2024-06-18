from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from haversine import haversine, Unit
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    __tablename__ = 'estado'

    abbreviation = Column(String(2), primary_key=True, name='sigla')
    range_start = Column(String(8), name='faixa_ini')
    range_end = Column(String(8), name='faixa_fim')
    name = Column(String(100), name='estado')
    capital = Column(String(100), name='capital')
    region = Column(String(100), name='regiao')
    name_without_accent = Column(String(100), name='estado_sem_acento')
    capital_without_accent = Column(String(100), name='capital_sem_acento')
    region_without_accent = Column(String(100), name='regiao_sem_acento')
    latitude = Column(String(50), name='latitude')
    longitude = Column(String(50), name='longitude')

    addresses = relationship('Address', back_populates='state', lazy='raise_on_sql')
    cities = relationship('City', back_populates='state', lazy='raise_on_sql')
    districts = relationship('District', back_populates='state', lazy='raise_on_sql')


class City(Base):
    __tablename__ = 'cidade'

    id = Column(Integer, primary_key=True, name='id_cidade')
    name = Column(String(100), name='cidade')
    name_without_accent = Column(String(100), name='cidade_sem_acento')
    state_abbreviation = Column(String(2), ForeignKey('estado.sigla'), name='estado')
    ibge_code = Column(String(20), name='cidade_ibge')
    area_code = Column(String(2), name='ddd')
    latitude = Column(String(50), name='latitude')
    longitude = Column(String(50), name='longitude')

    state = relationship('State', back_populates='cities')
    addresses = relationship('Address', back_populates='city', lazy='raise_on_sql')
    districts = relationship('District', back_populates='city', lazy='raise_on_sql')


class Neighborhood(Base):
    __tablename__ = 'bairro'

    neighborhood_id = Column(Integer, primary_key=True, index=True, name='id_bairro')
    name = Column(String(100), nullable=True, name='bairro')
    name_without_accent = Column(String(100), nullable=True, name='bairro_sem_acento')
    city_id = Column(Integer, nullable=True, name='cidade_id')
    state = Column(String(2), nullable=True, name='estado')
    latitude = Column(String(50), nullable=True, name='latitude')
    longitude = Column(String(50), nullable=True, name='longitude')

    addresses = relationship('Address', back_populates='neighborhood', lazy='raise_on_sql')


class District(Base):
    __tablename__ = 'distrito'

    id = Column(Integer, primary_key=True, name='id_distrito')
    name = Column(String(100), name='distrito')
    name_without_accent = Column(String(100), name='distrito_sem_acento')
    city_id = Column(Integer, ForeignKey('cidade.id_cidade'), name='cidade_id')
    state_abbreviation = Column(String(2), ForeignKey('estado.sigla'), name='estado')
    latitude = Column(String(50), name='latitude')
    longitude = Column(String(50), name='longitude')

    city = relationship("City", back_populates="districts", lazy='raise_on_sql')
    state = relationship("State", back_populates="districts", lazy='raise_on_sql')
    addresses = relationship("Address", back_populates="district", lazy='raise_on_sql')


class Address(Base):
    __tablename__ = 'logradouro'

    postal_code = Column(String(8), primary_key=True, index=True, name='cep')
    city_id = Column(Integer, ForeignKey('cidade.id_cidade'), nullable=False, name='cidade_id')
    state_abbreviation = Column(String(2), ForeignKey('estado.sigla'), nullable=False, name='estado')
    type = Column(String(50), nullable=False, name='tipo')
    street_name = Column(String(100), nullable=False, name='nome_logradouro')
    address = Column(String(100), nullable=False, name='logradouro')
    neighborhood_id = Column(Integer, ForeignKey('bairro.id_bairro'), nullable=True, name='bairro_id')
    district_id = Column(Integer, ForeignKey('distrito.id_distrito'), nullable=True, name='distrito_id')
    latitude = Column(String(20), nullable=False, name='latitude')
    longitude = Column(String(20), nullable=False, name='longitude')
    is_active = Column(String(1), nullable=False, name='cep_ativo')

    state = relationship('State', back_populates='addresses')
    city = relationship('City', back_populates='addresses')
    neighborhood = relationship('Neighborhood', back_populates='addresses')
    district = relationship('District', back_populates='addresses')

    def get_location(self):
        return float(self.latitude), float(self.longitude)

    def distance_to(self, location):
        distance = haversine(self.get_location(), location.get_location(), unit=Unit.KILOMETERS)
        if not distance:
            return None, "Could not calculate distance"
        return round(distance, 2), None
