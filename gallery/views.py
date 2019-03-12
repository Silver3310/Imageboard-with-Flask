from flask import render_template, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, logout_user, login_user, \
    login_required
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from gallery import app, db, models
from gallery.forms import LoginForm, RegistrationForm
from gallery.tools import upload_file_to_azure, list_files_in_azure, \
    delete_file_from_azure

Bootstrap(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

ALLOWED_EXTENSIONS = app.config["ALLOWED_EXTENSIONS"]


@login_manager.user_loader
def user_loader(user_id):
    return models.LoginUser.query.get(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('images'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.LoginUser.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            print("INVALID")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('images'))
    return render_template('login.html', title='Sign In', form=form)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("images"))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def process_file():
    if len(list(request.form.keys())) > 0 and request.form["delete"]:
        delete_file_from_azure(request.form["delete"])
        return redirect(url_for('images'))
    else:
        file = request.files["user_file"]

    if file.filename and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        upload_file_to_azure(file)
        return redirect(url_for('images'))

    else:
        return redirect(url_for('images'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.LoginUser(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/images')
def images():
    images_azure = list_files_in_azure()
    return render_template('images.html', images=images_azure)
