# Flask-Security Options
SECURITY_CONFIRMABLE = True
SECURITY_TRACKABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'

# Change this per app
SECURITY_EMAIL_SENDER = 'no-reply@localhost'
SECURITY_PASSWORD_SALT = 'use uuidgen on linux to generate a unique salt'
SECURITY_CONFIRM_SALT = 'use uuidgen on linux to generate a unique salt'
SECURITY_RESET_SALT = 'use uuidgen on linux to generate a unique salt'
SECURITY_LOGIN_SALT = 'use uuidgen on linux to generate a unique salt'
SECURITY_REMEMBER_SALT = 'use uuidgen on linux to generate a unique salt'

# Flask-Social configuration options
SOCIAL_TWITTER = {
    'consumer_key': 'twitter consumer key',
    'consumer_secret': 'twitter consumer secret'
}

SOCIAL_FACEBOOK = {
    'consumer_key': 'facebook app id',
    'consumer_secret': 'facebook app secret'
}