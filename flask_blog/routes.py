import secrets
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import os
from flask import render_template,url_for,flash,redirect
from flask_blog import app, db  
from flask_blog.forms import RegistrationForm, LoginForm, RForm
from flask_blog.models import User
import cv2
import glob
# import keras.backend.tensorflow_backend as tb
# import tensorflow as tf
# from tensorflow.keras.models import load_model
import keras

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
        # num =1
        # return "res"+ str(val(num))

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

# def auc(y_true, y_pred):
#     auc = tf.metrics.auc(y_true, y_pred)[1]
#     keras.backend.get_session().run(tf.local_variables_initializer())
#     return auc

def select(ch):
    ## Load Model 
    # tb._DISABLE_TRACKING.value = True
    # global graph
    # graph = tf.get_default_graph()
    # model = load_model('C://Users//Shivangi//Desktop//flask_blog//covid.h5', custom_objects={'auc': auc})
    model = load_model('C://Users//Shivangi//Desktop//flask_blog//covid.h5')
    # test_image = image.load_img('C://Users//Shivangi//Desktop//Covid_test-master//Covid_test-master//images//Test//covid//0.jpeg', 
    #                target_size=(64,64))

    imdir = 'C:/Users/Shivangi/Desktop/Covid_test-master/Covid_test-master/images/Test/non-covid/'
    ext = ['png', 'jpeg', 'gif', 'jpg']    # Add image formats here

    files = []
    [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]


    images = [cv2.imread(file) for file in files]
    image= images[-1]
    test_image= cv2.resize(image, (64, 64))

    # ### Image preprocessing
    def process(test_image):
        type(test_image)
    #     test_image=image.img_to_array(test_image)
        test_image=np.expand_dims(test_image,axis=0)
        return test_image
     
    # ###  Classifier
    def classifier(result,ch):
        if result[0][0] == 1.0:
    #             print('non-covid')
            ch='non-covid'
        else:
    #             print('covid')
            ch='covid'
        return ch


        # ### Predict
    test_image=process(test_image)
    result = classifier(model.predict(test_image),ch)
    
    
    return result

@app.route('/result')
def result():
    ch= " "
    s=select(ch)
    return render_template('result.html', title= 'results', s=s)

# @app.route('/ <int:num>')
# def result(num=1):
#     return "your code <hr> res" + str(val(num))
#     # return render_template('result.html', title= 'results')

# def val(num):
#     imdir = 'flask_blog/static/pro/'
#     ext = ['png', 'jpg', 'gif', 'jpeg']    # Add image formats here

#     files = []
#     [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]


#     images = [cv2.imread(file) for file in files]

#     cv2.imshow('title',images[-1])
#     cv2.waitKey(5000)
#     cv2.destroyAllWindows()
#     return ( str(num))

