from typing import Optional

from pydantic import BaseModel


class LocalizationDataModel(BaseModel):
    country: str
    city: str
    pickup_date: str
    dropoff_date: str


class CarDataModel(BaseModel):
    rent_company: str
    car_model: str
    license_plate: str
    rent_price: str
    rent_price_per_day: str


class RentDataModel(BaseModel):
    localization_data: Optional[LocalizationDataModel]
    car_data: Optional[CarDataModel]
