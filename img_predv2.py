#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:58:18 2020

@author: syntax
"""


import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
# from tensorflow.keras.layers import Input
# from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing import image

new_model= tf.keras.models.load_model('fruits.h5')
#new_model.summary()

path = input("Enter image path: ") #THIS IS THE DIRECTORY AND FILE FROM WHERE THE INPUT IMAGE (FROM CAMERA?) CAN BE FEEDED IN THE MODEL.

#FUNCTION WHICH RETURNS BOOLEAN VALUE.
def Fresh_or_Rotten(path):
    dire = '{}'.format(path)
    img = image.load_img(path, target_size=(20, 20))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = new_model.predict(images)
    if (classes[0][1] or classes[0][3] or classes[0][4])==1:
        check= True
    else:
	        check= False
    if check==True:
    		print("Fruit is Rotten.")
    else:
    		print("Fruit is fresh.")
    
check=Fresh_or_Rotten(path)
