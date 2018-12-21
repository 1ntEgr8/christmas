from flask import render_template, url_for, flash, redirect, request, session
from surprise.forms import RegistrationForm, AddRecepientForm
from surprise.models import Creator, Recepient
from surprise import app, db
from surprise import maketree
from datetime import datetime
import hashlib
import time

# change the format of the recepient list
# get that logic done for today, 
# then begin work on the reception part of the page

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
					   email=form.email.data)
		db.session.add(user)
		db.session.commit()
		session['first_name'] = form.first_name.data
		user = Creator.query.filter_by(first_name=form.first_name.data, email=form.email.data).first()
		session['user-id'] = user.id
		flash(f'santa has got your details {form.first_name.data}! Enter your recepients now ...', 'success')
		return redirect(url_for('add', name=session['first_name'], user_id=session['user-id']))
	return render_template('send.html', form=form)

@app.route('/add', methods=['GET','POST'])
def add():
	user = Creator.query.filter_by(id=session.get('user-id',0)).first()
	if user and not user.sent:
		if request.method == 'POST':
			names = request.form
			print(names)
			print("I AM HERE")
			count=0
			for name in names:
				if not count:
					count+=1
				else:
					print(names[name])
					print("ADDING RECEPIENT")
					recepient = Recepient(recepient_name=names[name],
									  date_posted=datetime.utcnow(),
									  image_file='static/gift_generated/'+str(session['user-id'])+'_'+str(count)+'.jpg',
									 creator_id=session['user-id'])
					db.session.add(recepient)
					db.session.commit()
					count+=1
					user.sent=True
			return redirect(url_for('link'))
	else:
		return redirect(url_for('home'))
	return render_template('add.html')

@app.route('/link', methods=['GET','POST'])
def link():
	first_name=session['first_name']
	user_id=session['user-id']
	return render_template('link.html',first_name=first_name, user_id=user_id)

@app.route('/receive/<string:first_name>/<int:user_id>', methods=['GET','POST'])
def receive(first_name, user_id):
	path = request.path
	creator_id = path[path.rfind('/')+1:]
	user = Creator.query.filter_by(id=creator_id).first()

	#add some validators
	name = user.first_name
	if request.method == 'POST':
		form = request.form
	return render_template('receive.html', first_name=name)

@app.route('/donate', methods=['POST'])
def donate():
	pass
	
