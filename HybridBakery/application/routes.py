from flask import render_template, session, redirect, request, url_for, flash
from application import app, service
#    , forms
from application.forms.basket import AddToBasketForm
from application.forms.registration import RegistrationForm
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from application import db
from application.forms.loginForm import LoginForm
from application.forms.registration import AddressForm
from application.models.address import Address
from application.models.product import Product
from application.models.customer import Customer
import os

from application.forms.enquiryForm import EnquiryForm
from application.models.enquiry import Enquiry


@app.route('/home', methods=['GET'])
def welcome():
    form = EnquiryForm()
    return render_template('home.html', title='Home', form=form)


@app.route('/home', methods=['GET', 'POST'])
def welcome_post():
    if request.method == 'POST':
        form = EnquiryForm(request.form)

        email_enquiry = form.email_enquiry.data
        full_name = form.full_name.data
        message = form.message.data

        customer = Customer.query.filter_by(email=email_enquiry).first()  # if this returns a user, then the email already exists in database

    if customer:
        new_enquiry = Enquiry(email_enquiry=email_enquiry, full_name=full_name, message=message,
                              email_id=customer.id)
        db.session.add(new_enquiry)
        db.session.commit()
        flash(f'Thanks for your enquiry {full_name}, we will be in touch shortly!')
        return redirect(url_for('welcome'))

    else:
        new_enquiry = Enquiry(email_enquiry=email_enquiry, full_name=full_name, message=message)
        db.session.add(new_enquiry)
        db.session.commit()
        flash(f'Thanks for your enquiry {full_name}, we will be in touch shortly!')
        return redirect(url_for('welcome'))


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
    stripe_keys = {
        'secret_key': os.environ['STRIPE_SECRET_KEY'],
        'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
    }
    products = service.get_checkout_products()
    if len(products) == 0:
        error = "There is nothing in your basket"
    for product in products:
        checkout_total += float(product.total)
    return render_template('checkout.html', products=products, checkout_total=checkout_total, message=error, key=stripe_keys['publishable_key'])

"""retired as added unnecessary extra step
@app.route('/payment')
def index():
    return render_template('payment.html',key=stripe_keys['publishable_key'])
"""

@app.route('/thankyou', methods=['POST'])
def thankyou():
    amount = checkout_total
    customer = stripe.Customer.create(
        email='sample@customer.com',
        source=request.form['stripeToken']
    )
    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='gbp',
        description='Hybrid Bakery Payment'
    )
    return render_template('thankyou.html', amount=amount)

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
    allergenslist = service.get_product_allergens(product.id)
    return render_template('product.html', product=product, form=form, allergenslist=allergenslist)
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

# @app.route('/orders', methods=['GET'])
# def show_orders():
#     error = ""
#     details = service.get_all_orders()
#     if details is None:
#         error = "There are no orders to display this week :("
#     return render_template('orders.html', order_detail=details, message=error)
#
#
# @app.route('/orders/madethisweek', methods=['GET'])
# def show_weekly_orders():
#     error = ""
#     details = service.get_this_weeks_orders()
#     if len(details) == 0:
#         error = "There are no orders to display this week :("
#     return render_template('weeks_orders.html', order_details=details, message=error)


# staff view only routes

@app.route('/orders', methods=['GET'])
@login_required
def show_orders():
    if current_user.user_role == "staff":
        error = ""
        details = service.get_all_orders()
        if details is None:
            error = "There are no orders to display this week :("
        return render_template('orders.html', order_detail=details, message=error)
    elif current_user.user_role == "client":
        return render_template('home.html')


@app.route('/orders/date/<time>', methods=['GET'])
@login_required
def show_orders_by_date(time):
    if current_user.user_role == "staff":
        error = ""
        details = service.get_orders_by_date(time)
        if len(details) == 0:
            error = "There are no orders to display this week :("
        return render_template('weeks_orders.html', order_detail=details, time=time, message=error)
    elif current_user.user_role == "client":
        return render_template('home.html')

@app.route('/orders/status/<order_status>', methods=['GET'])
@login_required
def show_orders_by_status(order_status):
    if current_user.user_role == "staff":
        error = ""
        details = service.get_orders_by_status(order_status)
        if details is None:
            error = "There are no orders to display"
        return render_template('order_status.html', order_detail=details, message=error)
    elif current_user.user_role == "client":
        return render_template('home.html')


# signup, profile, login routes

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

    # create a new client user with the form data. Hash the password so the plaintext version isn't saved.
    #new_customer = Customer(email=email, pass_word=generate_password_hash(password, method='sha256'), first_name = first_name, last_name=last_name, phone_number=phone_number, home_address_id=new_address.id, billing_address_id=new_address.id, user_role='client')

    # The next line of code will register a staff user - comment out the line above to use and signup a staff user to the DB
    new_customer = Customer(email=email, pass_word=generate_password_hash(password, method='sha256'), first_name = first_name, last_name=last_name, phone_number=phone_number, home_address_id=new_address.id, billing_address_id=new_address.id, user_role='staff')

    # add the new user to the database
    db.session.add(new_customer)
    db.session.commit()
    if form.validate_on_submit():
        flash(f'Success - account created for {form.first_name.data}!', 'success')
        return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    details = service.get_my_profile(current_user)
    recommendation = service.get_random()
    product = service.get_product(recommendation)
    return render_template('profile.html', customer=details, title='Profile', name=current_user.first_name, number=current_user.id, phone=current_user.phone_number, email=current_user.email, product = product )

@app.route('/myorders')
@login_required
def show_my_orders():
    error = ""
    details = service.get_my_orders(current_user)
    if details is None:
        error = "You have no orders to display. Why not take a look at our products for inspiration?"
    return render_template('myorders.html', title='My Orders', order_detail=details, name=current_user.first_name, message=error, number=current_user.id)

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


