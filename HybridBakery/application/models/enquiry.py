from application import db
from dataclasses import dataclass


@dataclass
class Enquiry(db.Model):
    id: int
    email_enquiry: str
    full_name: str
    message: str
    email_id: int

    id = db.Column(db.Integer, primary_key=True)
    email_enquiry = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(1000), nullable=False)
    email_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=True)
