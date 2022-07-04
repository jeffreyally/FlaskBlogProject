import os
from enum import unique
from smtplib import SMTP
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

#from models import User, Post
#from forms import RegistrationForm,LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ef274d49bf7ba7e8497d2686ebd6d853'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from app import routes