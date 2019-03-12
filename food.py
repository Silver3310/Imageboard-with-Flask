from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template(
        'food.html',
        food=food,
        list=[
            'pizza',
            'sushi',
            'quinoa'
        ]
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
