from application.models.product import Product
from application.models.order_details import Order_details

def get_products():
    return Product.query.all()

def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return product

def get_all_orders():
    return Order_details.query.all()

def get_this_weeks_orders():
    orders = Order_details.query.all()
    return orders