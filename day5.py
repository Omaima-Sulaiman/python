#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:27:25 2019

@author: omaima

"""
class Employee:
    def __init__(self,employee_number,name,address,salary,job_title):  
               self.__name=name
               self.employee_number=employee_number
               self.__address=address
               self.__salary=""
               self.__job_title=""
  
    def getName(self) :
       return self.__name
    
    def getAddress(self) :
       return self.__address
    def setAddress(self, new):
        self.__address=new
        return self.__address
       
   
    def getSalary(self) :
       return self.__salary
    
    def getJobTitle(self) :
       return self.__job_title
   
    def __del__( self ):
        print (self.__name+ 'I have been deleted')


employee1=Employee(1,'omaima','amman',800,'developer')

employee2=Employee(2,'haya','irbd',750,'manager')
print( employee1.employee_number)
print(employee2.employee_number,employee2.getAddress(),employee2.getJobTitle(),employee2.getName())
print("address"+"="+employee1.setAddress('USA'))


