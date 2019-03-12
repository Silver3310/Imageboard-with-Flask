from flask import Flask, render_template, flash, request
from wtforms import Form, TextAreaField, StringField
from flask_bootstrap import Bootstrap


# App config
DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'


class NameForm(Form):
    name = StringField('Name:')


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = NameForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        flash('Hello ' + name)
    return render_template(
        'hello.html',
        form=form
    )






