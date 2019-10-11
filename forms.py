from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number', validators= [Length(max=11)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    phone_number = StringField('2fa', validators= [Length(max=11)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SpellCheckForm(FlaskForm):
    checktext = StringField('Enter Text to Spell Check', validators=[DataRequired()])
    submit = SubmitField('Submit')