from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class MyForm(Flask):
    name = StringField('Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember me')
    salary = DecimalField('Salary', validators=[InputRequired])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female','Female')])
    country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'), ('UK', 'United Kingdom')])
    message = TextAreaField('message', validators=[InputRequired()])
    photo = FileField('Photo')
    
    