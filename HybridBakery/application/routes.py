from flask import render_template

from application import app, service


@app.route('/home', methods=['GET'])
def welcome():
    return 'Welcome to The Hybrid Bakery!'


@app.route('/products', methods=['GET'])
def show_products():
    error = ""
    details = service.display_products()
    if len(details) == 0:
        error = "There are no products to display"
    return render_template('product.html', product=details, message=error)


@app.route('/bakes/<int:id>')
def show_bake(id):
    return render_template('bake.html', bake = service.get_bake(id), message='What a tasty bake.')


