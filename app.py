from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import base64

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vapecloud.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)


class Guest(db.Model):
    __tablename__ = 'main_page'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    # TODO: Add Fields

    def __repr__(self):
        return '<Guest %r>' % self.parametr


class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    sale = db.Column(db.Integer, nullable=True)  # можно и false поставить
    connection_id = db.Column(db.Integer, nullable=False)
    volume = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Products %r>' % self.id


class Images(db.Model):
    __tablename__ = 'images'
    img_id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    depend_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    image = db.Column(db.BLOB, nullable=True)

    def __repr__(self):
        return '<Images %r>' % self.depend_id


class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(300), nullable=False)
    delivery = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    payment_method = db.Column(db.Integer, nullable=False)
    sale = db.Column(db.Integer, nullable=False)
    pre_price = db.Column(db.Integer, nullable=False)
    final_price = db.Column(db.Integer, nullable=False)
    order_time = db.Column(db.DateTime, default=datetime.utcnow)
    others = db.Column(db.Text, nullable=True)
    products_order_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        return '<Users %r>' % self.order_id


class OrderProducts(db.Model):
    __tabelname__ = 'order_products'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    order_depend = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.order_depend




@application.route('/')
@application.route('/home')
def show_main_page():
    # TODO here we must get all items in variables, because home page = catalog

    render_template('home.html')


@application.route('/item/<item_id>')
def show_item_page(item_id):
    # TODO define item selector
    item = None
    render_template('item.html', item=item)


@application.route('/add_new_items')
def show_add_page():
    # TODO define password input and checking.
    # Redirect to admin panel if password is ok else 
    # redirect to main page and send telegram message that 
    # somebody try enter

    render_template('add_new_items.html')


@application.route('/cart')
def show_cart_page():
    # TODO i don't know how but here we must define items, which user
    # were saved in his card and show it
    # 
    # must use cookies
    #
    # it will be comfortable if cart = [item, item, item, item, ...]
    #
    cart = None

    render_template('cart.html', cart=cart)


if __name__ == "__main__":
    # application.run(host='0.0.0.0', debug=False)
    application.run(debug=True)
