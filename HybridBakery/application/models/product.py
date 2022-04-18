from application import db
from dataclasses import dataclass


# the annotation below will help to turn the Python object into a JSON object
@dataclass
class Product(db.Model):
    # the declarations below are important for turning the object into JSON
    id: int
    product_name: str
    price: float
    product_description: str

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Numeric, nullable=True)
    product_description = db.Column(db.String(300), nullable=True)
