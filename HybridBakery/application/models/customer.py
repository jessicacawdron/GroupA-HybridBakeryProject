from application import db
from dataclasses import dataclass


@dataclass
class Customer(db.Model):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    home_address_id: int
    billing_address_id: int

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(35), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    home_address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    billing_address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)

