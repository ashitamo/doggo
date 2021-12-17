import tensorflow as tf
from tensorflow.keras import layers, models,utils
import numpy as np
import os
from PIL import Image, ImageFile

def get_model(input_shape,out):
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), padding='same',activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    #model.add(layers.Dropout(0.5))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(out))
    model.summary()
    return model

def get_train_data(img_folder,size):
    x_train=[]
    y_train=[]
    counter=-1
    for r,d,f in os.walk(img_folder):
        print(r.replace(img_folder,''))
        for i in f:
            img_path=r+'/'+i
            img = Image.open(img_path).resize(size).convert('RGB')
            img=np.array(img).astype('float32')
            x_train.append(img)
            y_train.append(counter)   
        counter+=1
    return np.array(x_train),utils.to_categorical(np.array(y_train)),counter


img_folder='imgs/'
input_shape=(224,224,3)
x_train,y_train,out_cls=get_train_data(img_folder,input_shape[:-1])

model=get_model(input_shape,out_cls)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=10,batch_size=4)#, validation_data=(test_images, test_labels))
model.save('m2.h5')
#test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)