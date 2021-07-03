#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


input=cv2.imread(r"C:\\Users\\prasa\\OneDrive\\Desktop\\photo.JPG",-1) # to read/ load an image   
# 0 indicates gray scale image
#1 indicates colour image
#-1 indiactes colour image with alpha channel
print(input)


# In[ ]:





# In[3]:


#input2=cv2.imread("nasa_3.jpg")   # nasa_3 pic since i changed from heic to jpg, the image is corrupted.(may be)


# In[4]:


cv2.imshow("cinemark pic_1", input)  #first parameter is title of image and second is image variable
cv2.waitKey(1000)   #for 1000ms image will shown and then destroy
cv2.destroyAllWindows()


# In[5]:


cv2.imshow("cinemark pic_2", input)  #first parameter is title of image and second is image variable
k=cv2.waitKey() 
if k==27:#until we press any key on keyboard , imag will be shown
    cv2.destroyAllWindows()
elif k==ord("d"):
    cv2.imwrite("photo_3.jpeg",input)
    cv2.destroyAllWindows()
    


# In[6]:


import numpy as np
print(input.shape)    #(a,b,c)  a-height  b-width  c-no.of channels
#since it is a colour image  it has 3 channels
#height and width are in pixels


# In[7]:


cv2.destroyAllWindows()


# In[8]:


print("height:{0} and width:{1}".format(input.shape[0],input.shape[1]))


# In[9]:


cv2.imwrite("output.png",input) # we can save images in different formats


# In[10]:


cv2.imwrite("output2.jpeg",input)


# In[11]:


import numpy as np
np.ones((1,4,3))


# In[12]:


np.empty((2,7))


# In[13]:


np.arange(1,5,2)     #(b/w 1 to 5 in steps of 2)


# In[14]:


np.linspace(1,5,4)  # 4 numbers from 1 to 5


# In[ ]:





# In[ ]:




