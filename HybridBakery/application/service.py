from application.models.product import Product
from application.models.order_detail import Order_detail

# putting this script here for future use as will need sessions when we ask users to log in
#engine = create_engine('mysql+pymysql://root@localhost/hybrid_bakery', echo=True)
#Session = sessionmaker(bind=engine)
#session = Session()
def get_products():
    return Product.query.all()

def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return product

def get_product_by_name(product_name):
    product = Product.query.filter_by(product_name=product_name).first()
    return product

def get_all_orders():
    return Order_detail.query.all()

def get_this_weeks_orders():
    orders = Order_detail.query.all()
    return orders