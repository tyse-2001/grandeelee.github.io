from app import app
from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, current_user, login_required
import csv
from model import User
from forms import LoginForm

all_packages = []
with open("./staycation.csv", 'r') as f:
    line = csv.reader(f, delimiter=",")
    _ = next(line)
    for row in line:
        all_packages.append(
            {
                "hotel_name": row[0],
                "duration": row[1],
                "packageCost": row[2],
                "image_url": row[3],
                "description": row[4],
            }
        )

def get_package(hotel_name):
    for package in all_packages:
        if package["hotel_name"] == hotel_name:
            break
    return package

@app.route('/')
@app.route('/index')
@app.route('/homepage')
def home():
    return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('packages'))
    form = LoginForm()
    if form.validate_on_submit():
        # email = request.form.get('email')
        # password = request.form.get('pswd')
        # remember = request.form.get('remember')
        check_user = User.getUser(form.email.data)
        if not check_user:
            form.email.errors.append("email not found")
            return render_template("login.html", form=form)
            # also need check 
        elif not check_user.checkPassword(check_user.password, form.password.data):
            form.password.errors.append("password incorrect")
            return render_template("login.html", form=form)
        else:
            login_user(check_user, remember=form.remember.data)
            flash("you are logged in")
            return redirect(url_for('packages'))

    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/packages')
@login_required
def packages():
    return render_template('packages.html', data=all_packages)

@app.route("/viewPackageDetail/<hotel_name>")
def viewHotel(hotel_name):
    package = get_package(hotel_name)
    return render_template("packages.html", data = [package])

@app.route("/book/<hotel_name>")
def book(hotel_name):
    # get the package detail
    # get check in/out date
    return render_template("login.html")

@app.route("/registration", methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        pswd = request.form.get('pswd')
        name = request.form.get('name')
        User.createUser(email, name, pswd)
        return render_template('registration.html')

    if request.method == 'GET':
        return render_template('registration.html')