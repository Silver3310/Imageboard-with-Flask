from gallery import db

db.create_all()


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

