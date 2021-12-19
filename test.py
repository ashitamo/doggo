import numpy as np
import os
from PIL import Image, ImageFile

emotion='sad'
img_folder=f'imgs/{emotion}/'
for i,n in enumerate(os.listdir(img_folder)):
    print(img_folder+n,img_folder+f'{emotion}{i}.' + n.split('.')[-1])
    os.rename(img_folder+n,img_folder+f'{emotion}{i}.' + n.split('.')[-1])
        #print(img_path)
        # img = Image.open(img_path).resize(size).convert('RGB')
        # img=np.array(img).astype('float32')