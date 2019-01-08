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


var1 = Genre()         #Genre() function will return the value of genre attribute to var1
var2 = Singer()        #Singer() function will return the value of singer attribute to var2
var3 = ReleasedYear()  #ReleasedYear() function will return the value of releasedYear attribute to var3

#Making use of if-else construct 
if(var1=="Classic" and var2=="Arijit Singh" and var3==2013):
    b= True
else:
    b=False

#printing the values for more clarity
print(var1)
print(var2)
print(var3)
print(b)
    
  
