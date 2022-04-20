from flask import render_template

from application import app, service


@app.route('/home', methods=['GET'])
def welcome():
    return 'Welcome to The Hybrid Bakery!'


@app.route('/products', methods=['GET'])
def show_products():
    error = ""
    details = service.get_products()
    if len(details) == 0:
        error = "There are no products to display"
    return render_template('products.html', product=details, message=error)


@app.route('/products/<int:id>')
def show_product(id):
    return render_template('product.html', product = service.get_product(id), message='What a tasty bake.')


