from application.models.product import Product


def display_products():
    return Product.query.all()


def get_bake(id):
    bake = Product.query.filter_by(id=id).first()
    return bake

