#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:01:14 2019

@author: omaima


import numpy as np
b = np.array([[1, 4, 7, 5],[2,4,5,6]])
print(b)
"""
import numpy as np
"""
a= np.arange(12).reshape(3,4)
print(a)
print("a size :",a.size)
print ("a shape: ", a.shape)
print ("a shape: ", a.ndim)
print ("a shape: ", a.dtype.name)
print ("a shape: ", a.itemsize)

g= np.ones( (2,4) , dtype=np.int16 )*6
print (g)

import numpy as np
a =np.array([[3,7,2,1,8,7,19,15],[10,2,7,4,5,5,9,1]])
print('a array:')
print (a)
print('\n quicksort:')
print (np.sort(a,kind='quicksort') )
print('\n mergesort')
print (np.sort(a,kind='mergesort') )
print('\n heapsort:')
print (np.sort(a,kind='heapsort') )
print('\n sort as flattened arra:')
print (np.sort(a,axis=None) ) 
"""
import matplotlib.pyplot as plt
"""
plt.style.use('ggplot')
f=[2,4,3,4,3]
w=[2,4,4,6,7]
plt.plot(f,w)
plt.show()
"""

# =============================================================================
# Q1
# =============================================================================
e= np.zeros( (10) )
print (e)
e1= np.ones( (10) )*5
print (e1)
g= np.ones( (10) )
print(g)

# =============================================================================
# Q2 
# =============================================================================
i = np.arange( 30,70 )
print(i)

# =============================================================================
# Q3
# =============================================================================
i = np.arange( 30,70,2 )
print(i)

# =============================================================================
# Q4
# =============================================================================
e= np.identity(3)
print(e)

# =============================================================================
# Q5
# =============================================================================

X = np.random.random(1)
print(X)

# =============================================================================
# Q6
# =============================================================================

i=np.arange(12).reshape(3,4)
print (i)


# =============================================================================
# Q7
# =============================================================================
i = np.arange( 0,20 )
print(i,i[9:16]*-1)

# =============================================================================
# Q8
# =============================================================================

x=[1,8,3,5]
y=np.random.randint(0,11,4)
print(x*y)

# =============================================================================
# Q9

# =============================================================================
o=np.arange(12).reshape(3,4)
print (o, o.shape)

# =============================================================================
# Q10
# =============================================================================
x = np.random.random((3, 3, 3))
print(x)

# =============================================================================
# Q11
# =============================================================================
a =np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,17,9]])
print("a-b: ",a-b)
print("a*b: ",a*b)
print("a.dot(b): ",a.dot(b))
print("a*2: ",a*2)
print("np.sin(a): ",np.sin(a))
print("a<3: ",a<3)
print("a.sum(): ",a.sum())
print("a.sum(axis=0): ",a.sum(axis=0))
print("c.sum(): ",c.sum())
print("c.sum(axis=0): ",c.sum(axis=0))
print("a.min(): ",a.min())
print("a.max(): ",a.max())
print("a.mean(): ",a.mean())
print("a average(): ",np.average(a))
print("a median(): ",np.median(a))
print("a std(): ",np.std(a))
print("a var(): ",np.var(a))
print("c.cumsum(): ",c.cumsum())
print("a[1:2] : ",a[1:2])
print("a[2:] : ",a[2:])
print("c[-1] : ",c[-1])


# =============================================================================
# Q12
# =============================================================================
x=range(1,50)
y=[value*3 for value in x]
plt.plot(x,y)
plt.title('Draw Line')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.show()

# =============================================================================
# Q13
# =============================================================================
x1=[10,20,30]
y1=[20,40,10]
x2=[10,20,30]
y2=[40,10,30]
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.title('two or more lines on same plot')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.legend(['line1', 'line2'])
plt.show()

# =============================================================================
# Q14
# =============================================================================
t=np.arange(0.,5.,0.2)
t2=t**2
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3,
'g^')
plt.show()

# =============================================================================
# Q15
# =============================================================================
objects = ('Python', 'Java', 'PHP', 'JavaScript', 'C#','C++')
y_pos = np.arange(len(objects))
popularity = [22.2,17.6,8.8,8,7.7,6.7]
plt.bar(y_pos, popularity, align='center', color=['red','black','green','blue','yellow','blue'])
plt.xticks(y_pos, objects)
plt.ylabel('PopulartiY')
plt.title('PopulartiY of Programming Language')
plt.show()


