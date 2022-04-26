from application import db
from dataclasses import dataclass


@dataclass
class ProductAllergen(db.Model):

    id: int
    product_id: int
    allergen_id: int

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    allergen_id = db.Column(db.Integer, db.ForeignKey("allergen.id"), nullable=False)