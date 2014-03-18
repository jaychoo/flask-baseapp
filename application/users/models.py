from application.core import db, app
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin

# Define User and Role models (that Flask-Security expects)
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    # Role based security via Flask-Security
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    # Base Flask-Security columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    # Flask-Security column for confirming users (SECURITY_CONFIRMABLE)
    confirmed_at = db.Column(db.DateTime())

    # Flask-Security column for tracking users (SECURITY_TRACKABLE)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(length=40))
    current_login_ip = db.Column(db.String(length=40))
    login_count = db.Column(db.Integer())


# Setup Flask-Security
app.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, app.user_datastore)