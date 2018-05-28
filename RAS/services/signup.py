from flask import Flask,render_template
app = Flask(__name__)

@app.route('/signup',method=['POST','GET'])
def signup():
	if method=="POST":
		name=request.form['name']
def login():
	if method=="POST":
		name=request.form['name']

if __name__ == '__main__':
	app.run(host='localhost',port=8001,debug=True)