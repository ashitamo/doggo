import tensorflow as tf
from tensorflow.keras import layers, models,utils
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
import os,random
from PIL import Image, ImageFile

def get_model(input_shape,out=3):
    model = models.Sequential()
    model.add(Conv2D(filters=16, kernel_size=(3, 3), padding='same', input_shape=input_shape, activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=24, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.333))
    model.add(Conv2D(filters=48, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Dropout(0.333))
    
    model.add(Conv2D(filters=96, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    #model.add(Dropout(0.33))
    model.add(Dense(out, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])
    model.summary()
    return model

def get_train_data(img_folder,size):
    convert='1'
    x_train=[]
    y_train=[]
    counter=-1
    for r,d,f in os.walk(img_folder):
        print(r.replace(img_folder,''))
        for i in f:
            img_path=r+'/'+i
            img = Image.open(img_path).resize(size).convert(convert)
            img=np.array(img).astype('float32')
            #img=[img[0]]
            x_train.append(img)
            y_train.append(counter)   
        counter+=1
    return np.array(x_train),utils.to_categorical(np.array(y_train))


img_folder='imgs/'
input_shape=(224,224,1)
categore=3
x_train,y_train=get_train_data(img_folder,input_shape[:-1])
x_train=x_train.reshape(-1,input_shape[0],input_shape[1],input_shape[2])

x=int(len(x_train)*(1-0.25))
x_train,x_train_val=x_train[:x],x_train[x:]
y_train,y_train_val=y_train[:x],y_train[x:]
index = [i for i in range(len(x_train))]
random.shuffle(index)
x_train=x_train[index]
y_train=y_train[index]
model=get_model(input_shape,categore)

history = model.fit(x_train, y_train, epochs=100,batch_size=24, validation_data=(x_train_val, y_train_val))
model.save('m2.h5')
#test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)