from flask import render_template, session, redirect, request, url_for, flash
from application import app, service
#    , forms
from application.forms.basket import AddToBasketForm
from application.forms.registration import RegistrationForm
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from HybridBakery.application import db
from HybridBakery.application.forms.loginForm import LoginForm
from HybridBakery.application.forms.registration import AddressForm
from HybridBakery.application.models.address import Address
from HybridBakery.application.models.customer import Customer


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


@app.route('/signup')
def signup():
    form = RegistrationForm()
    return render_template('registration.html', title='Signup', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup_post():

    if request.method == 'POST':
        form = RegistrationForm(request.form)

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data

        first_line = form.first_line.data
        second_line = form.second_line.data
        town = form.town.data
        postcode = form.postcode.data

        customer = Customer.query.filter_by(email=email).first()  # if this returns a user, then the email already exists in database

    if customer:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('signup'))

    new_address = Address(first_line=first_line, second_line=second_line, town=town, postcode=postcode)
    db.session.add(new_address)
    db.session.commit()

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.

    new_customer = Customer(email=email, pass_word=generate_password_hash(password, method='sha256'), first_name = first_name, last_name=last_name, phone_number=phone_number, home_address_id=new_address.id, billing_address_id=new_address.id)
    # add the new user to the database
    db.session.add(new_customer)
    db.session.commit()

    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile', name=current_user.first_name)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    # login code goes here
    if request.method == 'POST':
        form = LoginForm(request.form)
        email = form.email.data
        password = form.password.data

    customer = Customer.query.filter_by(email=email).first()
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not customer or not check_password_hash(customer.pass_word, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))  # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(customer)
    return redirect(url_for('profile'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome'))


