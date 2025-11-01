import cv2
import matplotlib.pyplot as plt
import numpy as np

def gauss(size, sigma):
    x,y=np.meshgrid(np.linspace(-size/2,size/2,size),\
                    np.linspace(-size/2,size/2,size))
    g=np.exp(-(x*x+y*y)/(2*sigma**2))
    g=g/np.sum(g)
    return g

test=[(3,1),(5,1),(15,1),
      (3,5),(5,5),(15,5),
      (3,10),(5,10),(15,10)]

fig,axes=plt.subplots(2,len(test),figsize=(20,10))
for i,(size,sigma)in enumerate(test):
    kernel_my=gauss(size,sigma)
    vector=cv2.getGaussianKernel(size,sigma)
    kernel_cv=np.outer(vector,vector)
    axes[0,i].imshow(kernel_my)
    axes[0,i].set_title(f'size={size}*{size},sigma={sigma}')
    axes[0,i].axis('off')
    axes[1,i].imshow(kernel_cv)
    axes[1,i].set_title(f'size={size}*{size},sigma={sigma}')
    axes[1,i].axis('off')
plt.tight_layout()
plt.show()