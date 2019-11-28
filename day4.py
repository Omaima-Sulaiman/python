#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:31:22 2019

@author: omaima

Q1
o=lambda x=1,y=2,z=3 :x+y+z
print(o())
print(o(10))
print(o(10,20))



Q2

from functools import reduce
llist=[2,3,4,5]
print(reduce(lambda a,b :a*b,llist))

Q3

q = lambda x, y : x * y
print ( q(56,7) )

Q4
mylist=[-1,-3,-5,1,4,6]
filtered = list( filter(lambda x: x < 0, mylist))
print(filtered)


Q5
x=lambda a,b,c :a+b+c
print(x(5,6,2))

Q6
x=("joey","monica","ross")
y=("chandler","pheobe")
z=("davaid","rachel","countney")
result=list(zip(x,y,z))
print(result)


Q7

coin=('bitcoin ','ether','ripple','litecoion')
code=('btc','eth','xrp','ltc ')
d= dict(zip(coin,code))
print(d)

Q8
def fun 
(var):
    letters=['a','b','i','o']
    if(var in letters):
        return true
    else:
        return false
sequence=['g','j','e','o,'p']
filtered=list(filter(fun,sequence))
print(filterd)   


Q9

x= list (map(int,input("enter a multiple value:").split()))
print("list of student:",x)

Q10

def newfunc(a):
    return a*a
x=list(map(newfunc,(1,2,3,4)))
print(x)

Q11

def func(a,b):
 return a+b
a=list(map(func,[2,4,5],[1,2,3,3,4]))
print(a)


Q12

c=map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))


Q13

c= filter(lambda x:(x>=3),map(lambda x:x+x ,(1,2,3,4)))
print(list(c))


Q14
lis = [ 14 , 34, 51, 36, 2, ] 
print (functools.reduce(lambda a,b : a if a < b else b,lis)) 

Q15

numbers=[1,2,3]
letters=['a','v','c']
results = tuple(map(lambda x, y: (x, y), numbers, letters))
print(results)

"""
    


     








