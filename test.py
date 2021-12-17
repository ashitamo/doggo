import numpy as np
import os
from PIL import Image, ImageFile

img_folder='imgs/'
for r,d,f in os.walk(img_folder):
    print(r)
    for i in f:
        img_path=r+'/'+i
        #print(img_path)
        # img = Image.open(img_path).resize(size).convert('RGB')
        # img=np.array(img).astype('float32')