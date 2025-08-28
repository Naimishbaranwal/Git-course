import os
import numpy as np
from PIL import Image
data = np.zeros((5,4,3),dtype=np.uint8)
data[:]=[255,255,0]
data[1:3]=[255,0,0]
data[:,2:3]=[0,0,255]
img=Image.fromarray(data,'RGB')
img.save('canvas.png')





 