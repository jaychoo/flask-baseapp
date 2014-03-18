import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'

# SQLAlchemy Options
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

# CSRF Settings
CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

# Recaptcha options
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

# SMTP Settings
MAIL_SERVER = "email-smtp.us-east-1.amazonaws.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "SMTP username"
MAIL_PASSWORD = "SMTP password"
MAIL_DEFAULT_SENDER = "do-not-reply@credacious.com"