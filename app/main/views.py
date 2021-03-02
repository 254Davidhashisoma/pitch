from flask import app
from flask import render_template

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='Home')


    @app.route('/about')
def about(): 
    return render_template('about.html',title='About')



@app.route('/account')
def account():
    return render_template('account.html',title='Account')


@app.route('/register')
def register():
    return render_template('register.html',title='Register')


@app.route('/login')
def login                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ():
    return render_template('login.html',title='Login')


