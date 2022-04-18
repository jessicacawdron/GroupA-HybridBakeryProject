from application import db
from dataclasses import dataclass


@dataclass
class Product(db.Model):

    id: int
    product_name: str
    price: float
    product_description: str

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=True)
    product_description = db.Column(db.String(300), nullable=True)
