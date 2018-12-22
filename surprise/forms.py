from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from surprise.models import Creator

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField("Let's add your recepients ->")

	def validate_email(self, email):
		user = Creator.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email has already been taken :( ')

class AddRecepientForm(FlaskForm):
	recepient_name = StringField()
	submit = SubmitField("Submit your order to Santa!")
