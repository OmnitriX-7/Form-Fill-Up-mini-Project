from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'