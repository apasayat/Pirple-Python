# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:36:01 2019

@author: abpasaya
"""

     
singer = "Arijit Singh"           #Name of the singer
genre = "Classic"                 #Genre of the song
releasedYear = 2013               #Year in which the song was released


def Genre():
    return genre
def Singer():
    return singer
def ReleasedYear():
    return releasedYear


var1 = Genre()
var2 = Singer()
var3 = ReleasedYear()

if(var1=="Classic" and var2=="Arijit Singh" and var3==2013):
    b= True
else:
    b=False

print(var1)
print(var2)
print(var3)
print(b)
    
  