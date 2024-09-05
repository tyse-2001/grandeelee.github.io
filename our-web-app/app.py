from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)  #__name__ = __main__

@app.route('/')
def home():
    return render_template('base.html', my_title="whatever")

@app.route("/<user_input>")
def greet(user_input):
    result = '<p>This is {}.<\p>'.format(user_input)
    return render_template('base.html', display_string=result)

@app.route("/greetWithArgs")
def greetWithArgs():
    name = request.args.get('friend').title()
    return redirect(url_for('greet', user_input=name))

@app.route("/submit_form", methods=['POST'])
def form():
    if request.method == 'POST':
        email = request.form.get('email')
        pswd = request.form.get('pswd')
        return render_template('base.html', email=email, pswd=pswd)