from application import db
from dataclasses import dataclass


@dataclass
class Allergen(db.Model):
    id: int
    allergen_type: str

    id = db.Column(db.Integer, primary_key=True)
    allergen_type = db.Column(db.String(50), nullable=False)
    