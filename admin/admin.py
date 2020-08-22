from flask import Blueprint, render_template, request, redirect, url_for, flash, session

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


def login_admin():
    session['admin_logged'] = 1


def isLogged():
    return True if session.get('admin_logged') else False


def logoutAdmin():
    session.pop('admin_logged', None)


@admin.route('/')
def index():
    # TODO here we must get all items in variables, because home page = catalog

    return render_template('admin/admin.html', title='ADMIN_PANEL')


@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin' and request.form['psw'] == '12345':
            login_admin()
            return redirect(url_for('.index'))
        else:
            flash("Неверный логин или пароль", "error")

    return render_template('admin/login.html', title='ADMIN_PANEL')


@admin.route('/logout', methods=['POST', 'GET'])
def logout():
    if not isLogged():
        return redirect(url_for('.login'))

    logoutAdmin()

    return redirect(url_for('.login'))

