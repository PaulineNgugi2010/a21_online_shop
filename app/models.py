from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db
from . import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    ''' Creates user '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        '''prevents access to password
        property
        '''
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        '''Sets password to a hashed password
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        '''Checks if password matches
        '''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: %r>' % self.username

    @login_manager.user_loader
    def load_user(user_id):
	    return User.query.get(int(user_id))


class Category(db.Model):
    ''' Creates product category '''
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.Text)


    def __repr__(self):
        return self.name


class Product(db.Model):
    ''' Creates an product '''

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    in_stock = db.Column(db.Boolean, default=True)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
                                 backref=db.backref('category',
                                                    lazy='dynamic'))

    def __repr__(self):
        return '<Product: %r>' % self.name