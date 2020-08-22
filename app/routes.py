from app import application
from flask import render_template


@application.route('/')
@application.route('/home')
def show_main_page():
    # TODO here we must get all items in variables, because home page = catalog

    return render_template('home.html')


@application.route('/item/<item_id>')
def show_item_page(item_id):
    # TODO define item selector
    item = None
    return render_template('item.html', item=item)


@application.route('/add_new_items')
def show_add_page():
    # TODO define password input and checking.
    # Redirect to admin panel if password is ok else
    # redirect to main page and send telegram message that
    # somebody try enter

    return render_template('add_new_items.html')


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

    return render_template('cart.html', cart=cart)