from flask_wtf import Form
from wtforms import StringField, SubmitField,TextAreaField,SelectField
from wtforms.validators import Required, Email,Length,Regexp,EqualTo

class EditProfileForm(Form):
	truename     = StringField('True name',validators=[Length(0,64)])
	location = StringField('Location', validators=[Length(0, 64)])
	about_me = TextAreaField('About me')
	submit   = SubmitField('Submit')

class EditProfileAdminForm(Form):
	username  = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
	'Usernames must have only letters, numbers, dots or underscores')])
	role      = SelectField('Role', coerce=int)
	truename  = StringField('True name', validators=[Length(0, 64)])
	location  = StringField('Location', validators=[Length(0, 64)])
	about_me  = TextAreaField('About me')
	submit    = SubmitField('Submit')
	def __init__(self, user, *args, **kwargs):
		super(EditProfileAdminForm, self).__init__(*args, **kwargs)
		self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
		self.user = user	
	def validate_username(self, field):
		if field.data != self.user.username and \
		User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')