from flask import render_template, session, redirect, request
from application import app, service
#    , forms
from HybridBakery.application.forms.basket import AddToBasketForm


@app.route('/home', methods=['GET'])
def welcome():
    return render_template('home.html')


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


@app.route('/products/<name>', methods=['GET', 'POST'])
def show_product(name, request=request):
    form = AddToBasketForm()
    product = service.get_product_by_name(name)
    if product is None:
        return render_template('error.html', error='Product')
    # filename = "{}.jpg".format(product_name)#
    session['visited'] = product.product_name
    if request.method == 'POST':
        session[product.product_name] = request.form.get('quantity')
        """
        if session.get("Basket") is None:
            session["Basket"] = [product.product_name]
        else:
            session["Basket"].append(product.product_name)
        """
    return render_template('product.html', product=product, form=form)
    # product_name = product_name, filename = filename,# '#

"""
@app.route('/products/<name>', methods=['POST'])
def add_product_basket(name):
    product = service.get_product_by_name(name)
    if product is None:
        return render_template('error.html', error='Product')
    # filename = "{}.jpg".format(product_name)#
    if session.get("Basket") is None:
        session["Basket"] = [product.product_name]
    else:
        session["Basket"].append(product.product_name)
    return render_template('product.html', product=product)
    # product_name = product_name, filename = filename,# '#
"""

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
