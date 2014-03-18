from application.core import db, app
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

# Define User and Role models (that Flask-Security expects)
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    ''' Role based security via Flask-Security '''
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    ''' User Model from Flask-Security '''
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

class Connection(db.Model):
    ''' Connection table for Oauth, via Flask-Social'''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)


# Setup Flask-Security and Flask-Social
app.user_datastore = SQLAlchemyUserDatastore(db, User, Role)
app.security = Security(app, app.user_datastore)
app.social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))