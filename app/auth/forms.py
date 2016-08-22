from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import Required, Email,Length,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
	username    = StringField('username', validators=[Required(), Length(1, 64)])
	password    = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit      = SubmitField('Log In')
class RegistrationForm(Form):
	username  = StringField('Username', validators=[Required(), Length(1, 64), \
		Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,\
		'Usernames must have only letters, numbers, dots or underscores')])
	password  = PasswordField('Password', validators=[Required(), \
		EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	about_me=StringField('About me',validators=[Length(0,64)])
	truename=StringField('True name',validators=[Required(),Length(1,64)])
	submit    = SubmitField('Register')
	
	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')

class UpdatePasswordForm(Form):
	oldpassword=PasswordField('oldpassword',validators=[Required()])
	password  = PasswordField('Password', validators=[Required(), \
		EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit    = SubmitField('Update password')