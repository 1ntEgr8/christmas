from datetime import datetime
from surprise import db

class Creator(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20))
	email = db.Column(db.String(120), unique=True, nullable=False)
	created = db.Column(db.Boolean, default=False)
	recepients = db.relationship('Recepient', backref='sender', lazy=True)

	def __repr__(self):
		return f"Creator('{self.first_name}', '{self.last_name}', '{self.email}', {self.created})"

class Recepient(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	recepient_name = db.Column(db.String(20), nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # no parentheses because we want to pass in the function as the argument
	creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)

	def __repr__(self):
		return f"Recepient('{self.recepient_name}','{self.image_file}','{self.date_posted}, '{self.creator_id}')"

