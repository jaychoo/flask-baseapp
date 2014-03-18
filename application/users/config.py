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