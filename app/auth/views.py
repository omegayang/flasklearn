from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user,logout_user,login_required,current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm,RegistrationForm,UpdatePasswordForm

@auth.before_app_request
def before_request():
	if current_user.is_authenticated:
		current_user.ping()
		#if request.endpoint[:5]!='auth.':
		#	return redirect(url_for('auth.nopower'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password.')
	return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data,
			password=form.password.data,
			truename=form.truename.data,
			about_me=form.about_me.data)
		db.session.add(user)
		flash('Registe successfully! You can now login the system.')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)

@auth.route('/updatepwd', methods=['GET', 'POST'])
@login_required
def uppwd():
	form = UpdatePasswordForm()
	if form.validate_on_submit():		
		if current_user.verify_password(form.oldpassword.data):
			current_user.password=form.password.data
			db.session.add(current_user)
			return redirect(url_for('main.index'))
			flash('password had been updated successfuly.')
		else:
			flash('Invalide password!')		
	return render_template('auth/update_password.html', form=form)

@auth.route('/nopower')
def nopower():
	return render_template('auth/nopwr.html')