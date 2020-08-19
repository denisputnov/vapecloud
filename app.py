from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///code.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

class Table1(db.Model):
     __tablename__ = 'table1'

    # TODO: Add Fields

     def __repr__(self):
        return '<Table1 %r>' % self.parametr

class Table2(db.Model):
     __tablename__ = 'table2'

    # TODO: Add Fields

     def __repr__(self):
        return '<Table2 %r>' % self.parametr

class Table3(db.Model):
     __tablename__ = 'table3'

    # TODO: Add Fields

     def __repr__(self):
        return '<Table3 %r>' % self.parametr

@application.route('/')
@application.route('/home')
def show_main_page():

    # TODO here we must get all items in variables, because home page = catalog
    
    render_template('home.html')


@application.route('/item/<ited_id>')
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
