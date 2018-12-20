from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
	last_name = StringField('Last Name', validators=[Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	no_of_recepients = IntegerRangeField('No of Recepients', validators=[DataRequired()], default=1)
	submit = SubmitField("Let's add your recepients ->")

class AddRecepientForm(FlaskForm):
	receipient_name = StringField('', validators=[DataRequired(), Length(min=2, max=20)])
