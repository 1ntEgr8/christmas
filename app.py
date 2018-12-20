from flask import Flask, render_template
import maketree

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/send')
def send():
	return render_template('send.html')

@app.route('/donate')
def donate():
	return render_template('donate.html')

if __name__ == "__main__":
	app.run(debug = True)