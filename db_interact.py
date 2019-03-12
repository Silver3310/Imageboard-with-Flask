from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sctqiewhhnvmer:74536945114a692e0b2c696d4824b5500cc9e1d8b0fdfaa08b3b746a6e8484e1@ec2-54-221-236-144.compute-1.amazonaws.com:5432/d2qcqv9deiss32'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Appuser(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    images = db.relationship(
        "Appimage",
        backref="appuser",
        lazy=True
    )

    def __repr__(self):
        return f'<Appuser {self.email}>'


class Appimage(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    URL = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    appuser_id = db.Column(
        db.Integer,
        db.ForeignKey('appuser.id')
    )

    def __repr__(self):
        return f'<Appimage {self.URL}: {self.appuser.email}>'
