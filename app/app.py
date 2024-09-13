from app import app
from flask import request, redirect, url_for, render_template, flash
import csv
from model import User

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
    return render_template('login.html', my_title="whatever")


@app.route('/packages')
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
def form():
    if request.method == 'POST':
        email = request.form.get('email')
        pswd = request.form.get('pswd')
        name = request.form.get('name')
        User.createUser(email, name, pswd)
        return render_template('registration.html')

    if request.method == 'GET':
        return render_template('registration.html')