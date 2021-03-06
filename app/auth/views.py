from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, login_required
from ..models import User
from forms import LoginForm, RegistrationForm
from . import auth
from .. import db

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(fullname = form.fullname.data,
                    email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully signed up! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title="Register")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid email or password.')
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', form=form, title="Login")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully signed out.')

    return redirect(url_for('main.home'))

