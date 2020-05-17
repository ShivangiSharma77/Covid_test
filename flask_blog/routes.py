from flask import render_template,url_for,flash,redirect
from flask_blog import app  
from flask_blog.forms import RegistrationForm, LoginForm, RForm
from flask_blog.models import User

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    form = RForm()
    if form.validate_on_submit():
        flash('Information Submitted', category='success')
        return redirect(url_for('home'))
    return render_template('home.html', title= 'Covid-19',form=form)
    

@app.route('/about')
def about():
    return render_template('about.html', title= 'About me')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title= 'Registration',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title= 'Login',form=form)
