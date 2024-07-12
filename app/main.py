from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app.db.models.address import Address
from app.db.session import SessionLocal
from app.schemas.address_schema import AddressRead, DistanceRead

app = FastAPI(
    description="API to get address by postal code and calculate distance between two postal codes",
    version="0.1.0",
    title="Address API",
    docs_url="/address",
    redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/address/healthcheck", tags=["Healthcheck"], description="Healthcheck endpoint", name="healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get(
    "/address/geolocation/distance/from/{from_postal_code}/to/{to_postal_code}",
    response_model=DistanceRead,
    tags=["Geolocation"],
    description="Get the distance between two postal codes",
)
def get_distance_between_postal_codes(from_postal_code: str, to_postal_code: str, db: Session = Depends(get_db)):
    from_address = db.query(Address).filter(from_postal_code == Address.postal_code).first()
    to_address = db.query(Address).filter(to_postal_code == Address.postal_code).first()
    if from_address is None or to_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    distance, error = from_address.distance_to(to_address)

    if error:
        raise HTTPException(status_code=400, detail=error)
    return {
        "distance": distance,
        "unit": "km",
        "from_address": from_address,
        "to_address": to_address,
        "method": "haversine"
    }


@app.get(
    "/address/postal/{postal_code}",
    response_model=AddressRead,
    tags=["Address"],
    description="Get address by postal code"
)
def get_address_by_postal_code(postal_code: str, db: Session = Depends(get_db)):
    address = db.query(Address).filter(postal_code == Address.postal_code).first()
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return address
