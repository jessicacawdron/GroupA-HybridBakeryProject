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

"""
retired route to make urls more user friendly
@app.route('/products/<int:id>')
def show_product(id):
    product = service.get_product(id)
    if product is None:
        return render_template('error.html', error='Product')
    #filename = "{}.jpg".format(product_name)#
    return render_template('product.html', product=product)
    #product_name = product_name, filename = filename,# '#
"""


@app.route('/products/<name>')
def show_product(name):
    product = service.get_product_by_name(name)
    if product is None:
        return render_template('error.html', error='Product')
    #filename = "{}.jpg".format(product_name)#
    return render_template('product.html', product=product)
    #product_name = product_name, filename = filename,# '#

@app.route('/orders', methods=['GET'])
def show_orders():
    error = ""
    details = service.get_all_orders()
    if details is None:
        error = "There are no orders to display this week :("
    return render_template('orders.html', order_details=details, message=error)

@app.route('/orders/madethisweek', methods=['GET'])
def show_weekly_orders():
    error = ""
    details = service.get_this_weeks_orders()
    if len(details) == 0:
        error = "There are no orders to display this week :("
    return render_template('weeks_orders.html', order_details=details, message=error)

