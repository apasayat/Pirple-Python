# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:32:57 2019

@author: abpasaya
"""
#Function to check euality of 2 numbers out of three
def Equality(a,b,c):
    if int(a) == int(b) or int(b) == int(c) or int(c) == int(a):
        return True
    else:
        return False


result = Equality(6,5,"5")
print(result)

result = Equality(5,"8",7)
print(result)