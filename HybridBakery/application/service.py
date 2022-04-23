from application.models.product import Product
from application.models.order_details import Order_details

# putting this script here for future use as will need sessions when we ask users to log in
#engine = create_engine('mysql+pymysql://root@localhost/hybrid_bakery', echo=True)
#Session = sessionmaker(bind=engine)
#session = Session()
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