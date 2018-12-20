from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
import hashlib
import maketree
from datetime import datetime

# set up the database
# get all the data you want onto the database
# boom. get a functional model today!

app = Flask(__name__)
app.config['SECRET_KEY']='a370792d9448746d6b8b0ad41a9e689c'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

class Creator(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20))
	email = db.Column(db.String(120), unique=True, nullable=False)
	no_of_recepients = db.Column(db.Integer, nullable=False)
	recepients = db.relationship('Recepient', backref='sender', lazy=True)

	def __repr__(self):
		return f"Creator('{self.first_name}', '{self.last_name}', '{self.email}', '{self.no_of_recepients}')"

class Recepient(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	recepient_name = db.Column(db.String(20), nullable=False)
	image_file = db.Column(db.String(20), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # no parentheses because we want to pass in the function as the argument
	creator_id = db.Column(db.Integer, db.ForeignKey('creator.id'), nullable=False)

	def __repr__(self):
		return f"Recepient('{self.recepient_name}','{self.image_file}','{self.date_posted}')"

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/send', methods=['GET','POST'])
def send():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'santa got your details {form.first_name.data}! Enter your recepients now ...', 'success')
		return redirect(url_for('add', hash_name=hashlib.sha256(form.first_name.data.encode()).hexdigest(), name=form.first_name.data, no_of_recepients=form.no_of_recepients.data))
	return render_template('send.html', form=form)

@app.route('/send/<string:name><int:no_of_recepients><string:hash_name>')
def add(hash_name, name, no_of_recepients):
	return render_template('add.html')

@app.route('/donate')
def donate():
	return render_template('donate.html')

if __name__ == "__main__":
	app.run(debug = True)