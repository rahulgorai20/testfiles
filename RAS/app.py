from flask import Flask,render_template
import pymongo
app = Flask(__name__)

@app.route('/home')
def index():

	return render_template('index.html')

@app.route('/signup')
def signup():

	return render_template('signup.html')
@app.route('/login')
def login():

	return render_template('login.html')
@app.route('/manager')
def manager():
	return render_template('manager.html')
@app.route('/member')
def member():
	return render_template('member.html')
@app.route('/incidents')
def incidents():
	return render_template('incidents.html')
@app.route('/changes')
def changes():
	return render_template('changes.html')
@app.route('/oncall')
def oncall():
	return render_template('oncall.html')

if __name__ == '__main__':
	app.run(host='localhost',port=8000,debug=True)