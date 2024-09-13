from flask import Flask, request, redirect, url_for, render_template, flash
import csv

app = Flask(__name__)  #__name__ = __main__

app.secret_key = "2g3hjkrfhjk34hj"  # necessary for the session cookie

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

@app.route("/login", methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        email = request.form.get('email')
        pswd = request.form.get('pswd')
        if email != "admin@abc.com" or pswd != "12345":
            flash("invalid credentials. please try again")
            return render_template('login.html')
        else:
            flash("you were successfully loggin in")
            return redirect(url_for('cards'))
    if request.method == 'GET':
        return render_template('login.html')