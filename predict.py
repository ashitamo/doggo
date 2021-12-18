from PIL import Image
import numpy as np
import os,shutil
import tensorflow as tf
from tensorflow.keras.models import load_model



model = load_model('m2.h5')

pre2=[]
oimg = Image.open(r'C:\Users\歐洲人\Desktop\archive\images\Images\n02096051-Airedale\n02096051_319.jpg')
img=oimg.resize((224,224)).convert('RGB')
img=np.array(img).astype('float32')
x_test=np.array([img])
result=model.predict(x_test)
print(result)