import cv2
import matplotlib.pyplot as plt
import numpy as np

def gauss(size, sigma):
    x,y=np.meshgrid(np.linspace(-size/2,size/2,size),\
                    np.linspace(-size/2,size/2,size))
    g=np.exp(-(x*x+y*y)/(2*sigma**2))
    g/=np.sum(g)
    return g

def blur(img,kernel):
    h,w=img.shape[:2]
    kh,kw=kernel.shape[:2]
    result=np.zeros((h-kh+1,w-kw+1,img.shape[2]),dtype=np.float32)
    for c in range(img.shape[2]):
        for k in range(h-kh+1):
            for l in range(w-kw+1):
                sum=np.zeros(img.shape[2],dtype=np.float32)
                for m in range(kh):
                    for n in range(kw):
                        sum[c]+=img[k+m,l+n,c]*kernel[m,n]
                result[k,l,c]=sum[c]
    return result

img=cv2.imread('Mona Lisa.jpg')
test=[[(3,1),(5,1),(15,1)],
      [(3,5),(5,5),(15,5)],
      [(3,10),(5,10),(15,10)]]

fig,axes=plt.subplots(3,4,figsize=(20,20))
axes[0,0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0,0].set_title('original image')
for i in range(3):
    axes[i,0].axis('off')

for j in range(1,4):
    for i,(size,sigma) in enumerate(test[j-1]):
        kernel=gauss(size,sigma)
        result=blur(img,kernel)
        result=np.clip(result,0,255).astype(np.uint8)
        axes[i,j].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        axes[i,j].set_title(f'size={size}*{size},sigma={sigma}')
        axes[i,j].axis('off')
plt.tight_layout()
plt.show()