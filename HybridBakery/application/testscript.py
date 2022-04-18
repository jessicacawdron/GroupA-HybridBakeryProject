from application import db

from application.models.product import Product

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:password@localhost/hybrid_bakery', echo=False, future=True)
Session = sessionmaker(bind=engine)

session = Session()


for product in session.query(Product).all():
    print(product.product_name, product.price, product.product_description)

