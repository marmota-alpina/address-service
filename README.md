

# Address API

API to get address by postal code and calculate distance between two postal codes
# Start up with docker

```bash
  docker-compose up --build
```
- The API will be available at http://localhost:8000
- The documentation will be available at http://localhost:8000 or http://localhost:8000/redoc
- The database will be available at http://localhost:5432
## Configuration
You can configure the API by setting the following environment variables on the `.env` file:
- `DATABASE_URL`: Database URL

## Endpoints

### Healthcheck

- **GET** `/healthcheck`
  - **Summary:** Healthcheck
  - **Description:** Healthcheck endpoint

### Get Distance Between Postal Codes

- **GET** `/geolocation/distance/from/{from_postal_code}/to/{to_postal_code}`
  - **Summary:** Get Distance Between Postal Codes
  - **Description:** Get the distance between two postal codes
  - **Parameters:**
    - `from_postal_code` (Path, Required): From Postal Code
    - `to_postal_code` (Path, Required): To Postal Code

### Get Address By Postal Code

- **GET** `/address/{postal_code}`
  - **Summary:** Get Address By Postal Code
  - **Description:** Get address by postal code
  - **Parameters:**
    - `postal_code` (Path, Required): Postal Code

## Responses

- **200 OK:** Successful Response
  - Content Type: `application/json`
  - Schema:
    - [AddressRead](#addressread)
    - [DistanceRead](#distanceread)
- **422 Unprocessable Entity:** Validation Error
  - Content Type: `application/json`
  - Schema:
    - [HTTPValidationError](#httpvalidationerror)

## Components

### Schemas

#### AddressRead

```json
{
  "postal_code": "string",
  "type": "string",
  "address": "string",
  "latitude": "string",
  "longitude": "string",
  "is_active": "string",
  "city": {
    "id": "integer",
    "name": "string"
  },
  "state": {
    "name": "string",
    "capital": "string",
    "region": "string",
    "abbreviation": "string"
  },
  "neighborhood": {
    "neighborhood_id": "integer",
    "name": "string"
  },
  "district": {
    "id": "integer",
    "name": "string"
  }
}
```

### DistanceRead
    
```json
    
{
  "distance": "number",
  "unit": "string",
  "method": "string",
  "from_address": {
    "postal_code": "string",
    "type": "string",
    "address": "string",
    "latitude": "string",
    "longitude": "string",
    "is_active": "string",
    "city": {
      "id": "integer",
      "name": "string"
    },
    "state": {
      "name": "string",
      "capital": "string",
      "region": "string",
      "abbreviation": "string"
    },
    "neighborhood": {
      "neighborhood_id": "integer",
      "name": "string"
    },
    "district": {
      "id": "integer",
      "name": "string"
    }
  },
  "to_address": {
    "postal_code": "string",
    "type": "string",
    "address": "string",
    "latitude": "string",
    "longitude": "string",
    "is_active": "string",
    "city": {
      "id": "integer",
      "name": "string"
    },
    "state": {
      "name": "string",
      "capital": "string",
      "region": "string",
      "abbreviation": "string"
    },
    "neighborhood": {
      "neighborhood_id": "integer",
      "name": "string"
    },
    "district": {
      "id": "integer",
      "name": "string"
    }
  }
}

 ```