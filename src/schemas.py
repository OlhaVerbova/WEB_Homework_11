from datetime import datetime, date

from pydantic import BaseModel, EmailStr


class ContactModel(BaseModel):
    first_name: str
    second_name: str
    email: EmailStr
    phone: str
    birth_date: date
    created_at: datetime
    updated_at: datetime


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    second_name: str
    email: EmailStr
    phone: str
    birth_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
