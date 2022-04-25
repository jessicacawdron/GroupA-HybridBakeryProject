from application import db
from dataclasses import dataclass


@dataclass
class Order_detail(db.Model):
    id: int
    customer_id: int
    order_value: float
    order_date: str
    order_status: str
    delivery_address_id: int
    delivery_recipient: str

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    order_value = db.Column(db.Numeric, nullable=False)
    order_date = db.Column(db.String(15), nullable=False)
    order_status = db.Column(db.String(35), nullable=False)
    delivery_address_id = db.Column(db.Integer, db.ForeignKey("address.id"), nullable=False)
    delivery_recipient = db.Column(db.String(100), nullable=False)
