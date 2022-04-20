from application import db

from application.models.product import Product
from application.models.allergen import Allergen
from application.models.product_allergen import Product_Allergen
from application.models.address import Address
from application.models.customer import Customer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:password@localhost/hybrid_bakery', echo=False, future=True)
Session = sessionmaker(bind=engine)

session = Session()


for product in session.query(Product).all():
    print(product.product_name, product.price, product.product_description)

address = session.query(Address).filter_by(id=1).first()
print(address.first_line, address.postcode)
for customer in address.home:
    print(customer.first_name, customer.last_name, 'lives at', address.first_line, address.postcode )
for customer in address.billing:
    print('The billing address for', customer.first_name, customer.last_name, 'is', address.first_line, address.postcode )
