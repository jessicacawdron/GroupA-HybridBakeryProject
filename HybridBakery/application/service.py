from application.models.product import Product
from application.models.order_detail import Order_detail
from application.models.allergen import Allergen
from application.models.product_allergen import ProductAllergen
from application.models.customer import Customer
from application.models.address import Address
from flask import session
from random import randint


# putting this script here for future use as will need sessions when we ask users to log in
#engine = create_engine('mysql+pymysql://root@localhost/hybrid_bakery', echo=True)
#Session = sessionmaker(bind=engine)
#session = Session()
from flask_login import current_user


def get_products():
    return Product.query.all()


def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return product


def get_product_by_name(product_name):
    product = Product.query.filter_by(product_name=product_name).first()
    return product


def get_checkout_products():
    output=[]
    for value in session:
        product=get_product_by_name(value)
        if product is not None:
            product.total = product.price*(int(session[product.product_name]))
            output.append(product)
    return output


def get_all_orders():
    return Order_detail.query.all()


def get_orders_by_date(time):
    if time == 'week':
        orders_by_date = Order_detail.query.filter(Order_detail.order_date.between('2022-04-28', '2022-05-05')).all()
    elif time == 'month':
        orders_by_date = Order_detail.query.filter(Order_detail.order_date.between('2022-04-05', '2022-05-05')).all()
    elif time == 'year':
        orders_by_date = Order_detail.query.filter(Order_detail.order_date.between('2021-05-05', '2022-05-05')).all()
    return orders_by_date


def get_orders_by_status(order_status):
    orders_by_status = Order_detail.query.filter_by(order_status=order_status).all()
    return orders_by_status


def get_product_allergens(product_id):
    allergens = []
    product_allergens = ProductAllergen.query.filter_by(product_id=product_id).all()
    for allergen in product_allergens:
        a = Allergen.query.filter_by(id=allergen.allergen_id).first()
        allergens.append(a)
    #allergenslist = Allergen.query.filter_by(allergen_id=allergens)
    return allergens

def get_my_orders(current_user):
    return Order_detail.query.filter_by(customer_id=current_user.id).all()

def get_my_profile(current_user):
    return Customer.query.filter_by(id=current_user.id).all()

def get_random():
    rand_num = randint(1,10)
    return rand_num


