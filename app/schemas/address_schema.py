from typing import Optional

from pydantic import BaseModel, Field, field_validator


class StateBase(BaseModel):
    name: Optional[str] = Field(None, alias='name')
    capital: Optional[str] = Field(None, alias='capital')
    region: Optional[str] = Field(None, alias='region')
    abbreviation: str = Field(..., alias='abbreviation')


class CityBase(BaseModel):
    id: Optional[int] = Field(None, alias='id')
    name: Optional[str] = Field(None, alias='name')


class NeighborhoodBase(BaseModel):
    id: Optional[int] = Field(None, alias='neighborhood_id')
    name: Optional[str] = Field(None, alias='name')


class DistrictBase(BaseModel):
    id: Optional[int] = Field(None, alias='id')
    name: Optional[str] = Field(None, alias='name')


class AddressBase(BaseModel):
    postal_code: str = Field(alias='postal_code')
    type: str = Field(alias='type')
    address: str = Field(alias='address', serialization_alias='address', description='Address')
    latitude: str = Field(alias='latitude')
    longitude: str = Field(alias='longitude')
    is_active: str = Field(alias='is_active', description='Is active Postal Code')
    city: Optional[CityBase] = Field(None, alias='city')
    state: Optional[StateBase] = Field(None, alias='state')
    neighborhood: Optional[NeighborhoodBase] = Field(None, alias='neighborhood')
    district: Optional[DistrictBase] = Field(None, alias='district')

    @field_validator('is_active')
    def convert_active_cep(cls, value):
        return 'Y' if value == 'S' else 'N'


class AddressRead(AddressBase):
    pass


class DistanceRead(BaseModel):
    distance: Optional[float] = Field(None, description='Distance between two addresses')
    unit: Optional[str] = Field(None, description='Distance unit, default is kilometers')
    method: Optional[str] = Field(None, description='Method used to calculate distance')
    from_address: Optional[AddressRead] = Field(None, description='Address of origin')
    to_address: Optional[AddressRead] = Field(None, description='Address of destination')
