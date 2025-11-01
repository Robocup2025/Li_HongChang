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

def pad_black(img,kernel):
    h,w=img.shape[:2]
    kh,kw=kernel.shape[:2]
    ph,pw=kh//2,kw//2
    pad_img=np.zeros((h+2*ph,w+2*pw,img.shape[2]))
    pad_img[ph:ph+h,pw:pw+w,:]=img
    return pad_img

def pad_wrap(img,kernel):
    h,w=img.shape[:2]
    kh,kw=kernel.shape[:2]
    ph,pw=kh//2,kw//2
    pad_img=np.zeros((h+2*ph,w+2*pw,img.shape[2]))
    pad_img[ph:ph+h,pw:pw+w,:]=img
    pad_img[0:ph,0:pw,:]=img[-1-ph:-1,-1-pw:-1,:]
    pad_img[0:ph,pw:pw+w,:]=img[-1-ph:-1,:,:]
    pad_img[0:ph,pw+w:pw*2+w,:]=img[-1-ph:-1,0:pw,:]
    pad_img[ph:ph+h,0:pw,:]=img[:,-1-pw:-1,:]
    pad_img[ph:ph+h,pw+w:pw*2+w,:]=img[:,0:pw,:]
    pad_img[ph+h:ph*2+h,0:pw,:]=img[0:ph,-1-pw:-1,:]
    pad_img[ph+h:ph*2+h,pw:pw+w,:]=img[0:ph,:,:]
    pad_img[ph+h:ph*2+h,pw+w:pw*2+w,:]=img[0:ph,0:pw,:]
    return pad_img

img=cv2.imread('Mona Lisa.jpg')
kernel=gauss(5,10)

fig,axes=plt.subplots(1,3,figsize=(20,15))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title('original image')
axes[0].axis('off')

pad_img_1=pad_black(img,kernel)
result_1=blur(pad_img_1,kernel)
result_1=np.clip(result_1,0,255).astype(np.uint8)
axes[1].imshow(cv2.cvtColor(result_1, cv2.COLOR_BGR2RGB))
axes[1].set_title('Zero Padding,size=5*5,sigma=10')
axes[1].axis('off')

pad_img_2=pad_wrap(img,kernel)
result_2=blur(pad_img_2,kernel)
result_2=np.clip(result_2,0,255).astype(np.uint8)
axes[2].imshow(cv2.cvtColor(result_2, cv2.COLOR_BGR2RGB))
axes[2].set_title('Wrap around,size=5*5,sigma=10')
axes[2].axis('off')

plt.tight_layout()
plt.show()