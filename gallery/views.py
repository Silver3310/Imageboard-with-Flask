from flask import render_template
from flask_bootstrap import Bootstrap
from gallery import app, models

Bootstrap(app)


@app.route('/images')
def images():
    images_q = models.Appimage.query.all()
    return render_template('images.html', images=images_q)
