from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SelectField, SubmitField, StringField, PasswordField, BooleanField, ValidationError, validators

from ..models import db, Category, Product
