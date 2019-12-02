#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:55:16 2019

@author: omaima


import sympy as sym
x = sym.symbols('x')
expr = x + 1
print ( expr.subs(x, 2) )

expr1 = x+x**2+1
print(expr1.subs(x,2))

from sympy import *
x = symbols('x')
init_printing()
expr=Integral(sqrt(1/x,x))
pprint(expr)


import sympy as sym
x = sym.Symbol('x')
y, i ,n, a, b = sym.symbols('y i n a b')

print( sym.expand( (x + y) ** 3 ) )
print(sym.simplify((x+x*y)/x)) 
print(sym.limit(sym.sin(x)/x,x,0))
print(sym.diff(x**4),x)
print( sym.integrate(6 * x ** 5, x))
print (sym.solve(x-1,x))
solution=sym.solve((x+5*y-2,-3*x+6*y-15),(x,y))
print(solution[x], solution[y])

print(sym.integrate(exp(x)*sin(x) +
exp(x)*cos(x), x))

print(sym.summation(1/2**i, (i, 0, sym.oo)))
print(sym.summation(1/log(n)**n,(n,2, sym.oo)))



from sympy import symbols
from sympy.plotting import plot3d

x,y = symbols('x y')
f=x**2*y**2

plot3d(f, (x, -5, 5),(y,-5,5))

 """
 

# =============================================================================
# Q1
# =============================================================================

from sympy import *
from sympy.plotting import *
x,y,z = symbols('x y z')
#a-
expr= x**2+x**3+21*x**4 + 10*x+1
print( expr.subs(x, 7) )
#b-
print(expand( (x + y) ** 2))
#c-
print(simplify(4*x**3+21*x**2+10*x+12))
#d-
print(limit(1/(x**2),x,oo))
#f-
print(integrate(sin(x)+exp(x)*cos(x)+tan(x),x))
#g-
print(factor(x**3 + 12*x*y*z +3*y**2*z) )
#h-
print(solveset(x-4,x))
#i-
m1 =Matrix([[5, 12, 40], [30, 70, 2]])
m2 =Matrix([2, 1, 0])
print( m1*m2 )
#j-
plot(x**3+3, (x, -10, 10))
#k-
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))


# =============================================================================
# Q2
# =============================================================================
import xlsxwriter
workbook = xlsxwriter.Workbook('example10.xlsx')
worksheet = workbook.add_worksheet()
worksheet.autofilter('A1:B1')
data = ["this is example"]
format = workbook.add_format()
format.set_font_color('red')
format.set_font_size(12)
worksheet.write_column('A1:B1', data ,format)
data2 = ["export my sheet"]
format = workbook.add_format()
format.set_font_color('black')
format.set_font_size(12)
worksheet.write_column('A2:B2', data2 ,format)
data3=[1,2]
data4=[3]
for elem in data3:
    format = workbook.add_format()
    format.set_font_color('black')
    format.set_font_size(12)
    worksheet.write_column("A3:A4", data3 ,format)
for elem in data4:
    format = workbook.add_format()
    format.set_font_color('red')
    format.set_font_size(12)
    worksheet.write_column("A5", data4 ,format)
workbook.close()


# =============================================================================
# Q3
# =============================================================================
from xlrd import open_workbook
wb = open_workbook('simple.xlsx')
for s in wb.sheets():
     print ("Sheet:", s.name)
     for row in range(s.nrows):
         values = []
         for col in range(s.ncols):
             values.append(s.cell(row,col).value)
             print(values)











































