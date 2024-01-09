from datetime import date
from src.database.models import Contact
from src.schemas import ContactModel
from sqlalchemy.orm import Session
from sqlalchemy import extract


async def get_contacts(limit: int, offset: int, db: Session):
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts


async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def get_contact_by_email(email: str, db: Session):
    contact = db.query(Contact).filter_by(email=email).first()
    return contact


async def get_contact_by_phone(phone: str, db: Session):
    contact = db.query(Contact).filter_by(phone=phone).first()
    return contact


async def get_contact_by_first_name(first_name: str, db: Session):
    contact = db.query(Contact).filter_by(first_name=first_name).first()
    return contact


async def get_contact_by_second_name(second_name: str, db: Session):
    contact = db.query(Contact).filter_by(second_name=second_name).first()
    return contact


async def get_contact_by_birth_date(birth_date: date, db: Session):
    contact = db.query(Contact).filter_by(birth_date=birth_date).first()
    return contact


async def create(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update(contact_id: int, body: ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.second_name = body.second_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birth_date = body.birth_date
        db.commit()
    return contact


async def remove(contact_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_contacts_birthday(start_date: date, end_date: date, db: Session):
    birth_day = extract('day', Contact.birth_date)
    birth_month = extract('month', Contact.birth_date)
    contacts = db.query(Contact).filter(
        birth_month == extract('month', start_date),
        birth_day.between(extract('day', start_date), extract('day', end_date))
    ).all()
    return contacts
