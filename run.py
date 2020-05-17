# from flask import Flask, render_template,url_for,flash,redirect
# from flask_sqlalchemy import SQLAlchemy
# from forms import RegistrationForm, LoginForm, RForm

# app = Flask(__name__)
# app.config['SECRET_KEY'] = '550e71fa3b4a0a957b395cb0e2f8642f'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
# def init_db():
#     db.init_app(app)
#     db.app = app
#     db.create_all()
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     # password= db.Column(db.String(60))

    # def __repr__(self):
    #     return ("User is - %s , Email is - %s " %(self.username, self.email))
        
# from models import User

# @app.route('/',methods=['GET','POST'])
# @app.route('/home',methods=['GET','POST'])
# def home():
#     form = RForm()
#     if form.validate_on_submit():
#         flash('Information Submitted', category='success')
#         return redirect(url_for('home'))
#     return render_template('home.html', title= 'Covid-19',form=form)
    

# @app.route('/about')
# def about():
#     return render_template('about.html', title= 'About me')

# @app.route('/register',methods=['GET','POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash('Account created', category='success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title= 'Registration',form=form)

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title= 'Login',form=form)
from flask_blog import app

if __name__ == '__main__':
    app.run(debug=True)

