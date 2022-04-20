from application import db
from dataclasses import dataclass


@dataclass
class Address(db.Model):
    id: int
    first_line: str
    second_line: str
    town: str
    postcode: str

    id = db.Column(db.Integer, primary_key=True)
    first_line = db.Column(db.String(100), nullable=False)
    second_line = db.Column(db.String(100), nullable=True)
    town = db.Column(db.String(35), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    home = db.relationship('Customer', primaryjoin="Address.id==Customer.home_address",
                                backref='customer')
    billing = db.relationship('Customer', primaryjoin="Address.id==Customer.billing_address", backref='customer')