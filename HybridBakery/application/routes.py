from flask import render_template, session, redirect, request
from application import app, service
#    , forms
from application.forms.basket import AddToBasketForm
from application.forms.registration import RegistrationForm


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


@app.route('/checkout', methods=['GET', 'POST'])
def show_basket():
    checkout_total= float(0.00)
    error = ""
    products = service.get_checkout_products()
    if len(products) == 0:
        error = "There is nothing in your basket"
    for product in products:
        checkout_total += float(product.total)
    return render_template('checkout.html', products=products, checkout_total=checkout_total, message=error)


@app.route('/registration', methods=['GET','POST'])
def register():
    form = RegistrationForm
    return render_template('registration.html', title='Registration', form=form)


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
    return render_template('orders.html', order_detail=details, message=error)


@app.route('/orders/madethisweek', methods=['GET'])
def show_weekly_orders():
    error = ""
    details = service.get_this_weeks_orders()
    if len(details) == 0:
        error = "There are no orders to display this week :("
    return render_template('weeks_orders.html', order_details=details, message=error)

