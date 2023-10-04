from flask import Flask, jsonify, request, redirect, url_for, session
from flask_session import Session
import os
from flask_cors import CORS
from flask import render_template, request, jsonify
from routes.users import users
import services.userService as userService
import services.dbService as dbService
from chat import getResponse


app = Flask(__name__,static_folder='static')
app.secret_key = 'super-secret'
CORS(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

if not os.path.isfile('maternity.db'):
    dbService.connect()

@app.get('/')
def index():
    form_data = None
    return render_template('index.html', form_data=form_data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form_data = None
        return render_template('register.html', form_data=form_data)
    else:
        form_data = request.form
        if userService.isEmailExists(form_data['email']):
            error_message = 'User with this email already exists.'
            return render_template('register.html', error_message=error_message, form_data=form_data)
        
        user = userService.insert({
            'name': form_data['name'],
            'email': form_data['email'],
            'password': form_data['password']
        })
        session['user'] = user

        return redirect(url_for('chat'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form_data = None
        return render_template('login.html', form_data=form_data)
    else:
        form_data = request.form
        user = userService.getUser(form_data['email'])

        if user is None:
            error_message = 'User with this email not found.'
            return render_template('login.html', error_message=error_message, form_data=form_data)
        
        if str(user[3]) != str(form_data['password']):
            error_message = 'Invalid Password.'
            return render_template('login.html', error_message=error_message, form_data=form_data)
        
        
        session['user'] = user

        return redirect(url_for('chat'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chat.html')
    else:
        message = request.form['message']
        return getResponse(message)
        


app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run( port=105, debug=True)