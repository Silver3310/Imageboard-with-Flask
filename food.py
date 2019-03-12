from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template(
        'food.html',
        food=food
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
