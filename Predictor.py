# ###  Import Essentials
from keras.preprocessing import image
import cv2
import numpy as np
from keras.models import load_model

### Load Model 
model = load_model('covid.h5')
test_image = image.load_img('C://Users//ajink//Documents//covid//X-ray-TeamProject//images//test//covid//7.jpeg', 
               target_size=(64,64))

# ### Image preprocessing
def  process(test_image):
    type(test_image)
    test_image=image.img_to_array(test_image)
    test_image=np.expand_dims(test_image,axis=0)
    return test_image

# ###  Classifier
def classifier(result):
    if result[0][0] == 1.0:
        print('non-covid')
    else:
        print('covid')

# ### Predict
test_image=process(test_image)
result = classifier(model.predict(test_image))