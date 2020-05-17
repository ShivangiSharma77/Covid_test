import secrets
import os
from flask import render_template,url_for,flash,redirect
from flask_blog import app, db  
from flask_blog.forms import RegistrationForm, LoginForm, RForm
from flask_blog.models import User

def save_picture(form_picture):
    random_hex = secrets.token_hex(8) 
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/pro', picture_fn)
    form_picture.save(picture_path)

    return picture_fn

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    form = RForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Information Submitted', category='success')
        return redirect(url_for('result'))
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

@app.route('/result')
def result():
    return render_template('result.html', title= 'results')