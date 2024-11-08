#!/usr/bin/env python
# coding: utf-8

# In[0]:
import numpy as np
from PIL import Image, ImageFilter
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# In[1]:

# lendo as cores
# red = Image.open( 'red.jpg' )
# blue = Image.open( 'blue.jpg' )
# yellow = Image.open( 'yellow.jpg' )
# orange = Image.open( 'orange.jpg' )
# purple = Image.open( 'purple.jpg' )
# green = Image.open( 'green.jpg' )
# white = Image.open( 'white.jpg' )
# black = Image.open( 'green.jpg' )


red = [255,0,0]
blue = [0, 255, 0]
yellow = [255, 255, 0]
orange = [255,165,0]
purple = [0, 255, 0]
green = [0, 128, 0]
white = [255, 255, 255]
black = [0, 0, 0]



# red_ = red.convert('RGB').getcolors()
# blue_ = blue.convert('RGB').getcolors()
# yellow_ = yellow.convert('RGB').getcolors()
# orange_ = orange.convert('RGB').getcolors()
# purple_ = purple.convert('RGB').getcolors()
# green_ = green.convert('RGB').getcolors()
# white_ = white.convert('RGB').getcolors()
# black_ = black.convert('RGB').getcolors()


# In[2]:

train_x=[red, blue, yellow, orange, purple, green, white, black]
train_y=["#FF0000", "#0000FF", "#FFFF00", "#FFA500", "#A020F0", "#008000", "#FFFFFF", "#000000"]

# i=0
# colors = []
# while i<8:
    
#     for color_rgb in train_x[i].getdata():
#         if color_rgb not in colors:
#             colors.append(color_rgb)
#     i+=1
# print(colors)
# train_x =np.asarray(colors)
print(train_x)
# In[3]:
modelo = LinearSVC()
modelo.fit(train_x, train_y)

# %%
train_y = np.asarray(train_y)
print(train_x.shape, train_y.shape)

# %%
print(train_x)
# %%
print(train_y)
# %%
