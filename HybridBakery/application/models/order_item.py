from application import db
from dataclasses import dataclass


@dataclass
class Order_item(db.Model):
    id: int
    order_id: int
    product_id: int
    quantity: int
    product_price: float

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order_detail.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_price = db.Column(db.Numeric, nullable=True)
