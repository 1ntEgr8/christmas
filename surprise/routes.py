from flask import render_template, url_for, flash, redirect
from surprise.forms import RegistrationForm
from surprise.models import Creator, Recepient
from surprise import app, db
from surprise import maketree
import hashlib

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
		user = Creator(first_name=form.first_name.data, 
					last_name=form.last_name.data,
					email=form.email.data,
					no_of_recepients=form.no_of_recepients.data)
		db.session.add(user)
		db.session.commit()
		flash(f'santa has got your details {form.first_name.data}! Enter your recepients now ...', 'success')
		return redirect(url_for('add', hash_name=hashlib.sha256(form.first_name.data.encode()).hexdigest(), name=form.first_name.data, no_of_recepients=form.no_of_recepients.data))
	return render_template('send.html', form=form)

@app.route('/send/<string:name><int:no_of_recepients><string:hash_name>')
def add(hash_name, name, no_of_recepients):
	return render_template('add.html')

@app.route('/donate')
def donate():
	return render_template('donate.html')
