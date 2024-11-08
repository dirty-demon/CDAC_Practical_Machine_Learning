# import required packages
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
import cv2

# get the dataset
data = tf.keras.datasets.fashion_mnist

# load the data from tf
(training_images, training_labels), (test_images, test_labels) = data.load_data()
# print(training_images[1])
print(training_labels[3])
cv2.imshow('image', training_images[3])
cv2.waitKey(0)
