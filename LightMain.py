#!/usr/bin/env python
# coding: utf-8

# In[0]:

from PIL import Image, ImageFilter
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# In[1]:

# lendo as cores
red = Image.open( 'red.jpg' )
blue = Image.open( 'red.jpg' )
yellow = Image.open( 'yellow.jpg' )
orange = Image.open( 'orange.jpg' )
purple = Image.open( 'purple.jpg' )
green = Image.open( 'green.jpg' )
white = Image.open( 'white.jpg' )
black = Image.open( 'green.jpg' )

red_ = red.convert('RGB').getcolors()
blue_ = blue.convert('RGB').getcolors()
yellow_ = yellow.convert('RGB').getcolors()
orange_ = orange.convert('RGB').getcolors()
purple_ = purple.convert('RGB').getcolors()
green_ = green.convert('RGB').getcolors()
white_ = white.convert('RGB').getcolors()
black_ = black.convert('RGB').getcolors()


# In[2]:

train_x=[red_, blue_, yellow_, orange_, purple_, green_, white_, black_]
train_y=["#FF0000", "#0000FF", "#FFFF00", "#FFA500", "#800080", "#008000", "#FFFFFF", "#000000"]

# In[3]:
modelo = LinearSVC()
modelo.fit(train_x, train_y)

# %%

vermelho =[]
vermelho = red.convert('RGB').getcolors()
print(vermelho)
# %%


type(train_y)
# %%
