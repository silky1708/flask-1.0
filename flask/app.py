from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request

from flask import redirect, url_for
app = Flask(__name__)

# [python -m flask run] to start development server
# python app.py runserver -d -> to run server in debug mode
@app.route('/hello/<name>', methods=['GET'])
def hello_there(name):
    return "Welcome {name}!".format(name=name)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to flask home!"

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('hello_there',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)
