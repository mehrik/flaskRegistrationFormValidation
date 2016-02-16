from flask import Flask, render_template, redirect, flash, request, session
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
app = Flask(__name__)
app.secret_key = "Maric Is Awesome"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    today = datetime.today()
    strToday = datetime.strftime(today, '%Y-%m-%d')
    today = datetime.strptime(strToday, '%Y-%m-%d')
    
    if len(request.form['email']) < 1:
        flash('Email field cannot be blank!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
    elif len(request.form['first_name']) < 1:
        flash('First name field cannot be blank!')
    elif len(request.form['last_name']) < 1:
        flash('Last name field cannot be blank!')
    elif not request.form['first_name'].isalpha():
        flash('First name field can only contain letters')
    elif not request.form['last_name'].isalpha():
        flash('Last name field can only contain letters')
    elif len(request.form['password']) < 8:
        flash('Password field must be at least 8 characters!')
    elif not re.search(r'\d', request.form['password']) or not re.search(r'[A-Z]', request.form['password']):
        flash('Password field must contain at least 1 capital letter and a number')
    elif request.form['password'] != request.form['confirm_pw']:
        flash('Passwords do not match')
    elif len(request.form['birthdate']) < 1:
        flash('Birthdate field cannot be blank!')
    elif datetime.strptime(request.form['birthdate'], '%Y-%m-%d') >= today:
        flash('Please enter a valid date, you cannot be born after today')
    else:
        flash('Success!')

    return redirect('/')

app.run(debug=True)