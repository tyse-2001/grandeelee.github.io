from app import app
from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, current_user, login_required
import csv
import re

# ====== models =======
from model import User, Package
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
        # if request.method == 'POST' and form.validate():
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
    
@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files.get("uploadFile")
        data = file.read().decode("utf-8").split("\n")
        file.close()
        datatype = request.form.get("dataType")
        if datatype == "packages":
            n = 0
            for line in data[1:]:
                hotel_name,duration,unit_cost,image_url,description = line.split(",")
                package = Package.getPackage(hotel_name.strip('"'))
                if package:
                    flash(f"Package {hotel_name} already exist")
                    continue
                Package.createPackage(hotel_name.strip('"'), int(duration), float(unit_cost), image_url, description.strip('"'))
                flash(f"Packages {hotel_name} created successfully")
                n += 1
            # here we store the data in the database
            flash(f"{n} packages uploaded successfully")

        
    return render_template("upload.html")