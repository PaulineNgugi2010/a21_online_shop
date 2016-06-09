from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SelectField, IntegerField, SubmitField, StringField, PasswordField, BooleanField, ValidationError, validators
from ..models import db, Category, Product
from wtforms.validators import Required, Length

class AddProductForm(Form):
  ''' Form for admins to add product '''
  name = StringField('Name', validators=[Required(), Length(1, 70)])
  description = StringField('Description', validators=[Required(), Length(1, 300)])
  price = IntegerField('Price', validators=[Required()])
  category = SelectField('Category',
                           [validators.Required(
                               message='Please select a category.')],
                           coerce=int)
  stock = IntegerField('Quantity of Item',validators=[Required()])
  submit = SubmitField('Save')

  def __init__(self, *args, **kwargs):
      super(AddProductForm, self).__init__(*args, **kwargs)
      self.category.choices = [
          (category.id, category.name) for category in Category.query.all()]


class AddCategoryForm(Form):
  name = StringField('Name', validators=[Required(), Length(1, 120)])
  description = StringField('Description', validators=[Length(1, 300)])
  save = SubmitField('Save')
