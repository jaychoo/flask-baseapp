from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

# Create Flask App Instance
app = Flask(__name__)
app.config.from_object('app.config')

# Create DB object
db = SQLAlchemy(app)

# Create Mail object
mail = Mail(app)

# Setup 404 handler
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Later on you'll import the other blueprints the same way:
# from app.users.views import mod as usersModule
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
# app.register_blueprint(usersModule)
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)