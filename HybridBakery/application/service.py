from application.models.product import Product


def get_products():
    return Product.query.all()


def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return product

