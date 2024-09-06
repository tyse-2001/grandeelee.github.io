from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)  #__name__ = __main__

app.secret_key = "2g3hjkrfhjk34hj"  # necessary for the session cookie

@app.route('/')
@app.route('/index')
@app.route('/homepage')
def home():
    return render_template('login.html', my_title="whatever")

@app.route("/<user_input>")
def greet(user_input):
    result = '<p>This is {}.<\p>'.format(user_input)
    return render_template('base.html', display_string=result)

@app.route('/cards')
def cards():
    with open('data.csv', 'r') as f:
        data = f.read().split('\n')
    data = [line.split(',') for line in data]

    return render_template('cards.html', data=data)

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