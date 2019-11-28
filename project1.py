#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:36:03 2019

@author: omaima
"""
import functools

class Person :
    def __init__(self,name,address):
        self._name=name
        self._address=address
    def getName(self):
        return self._name
    def setName (self,newName):
        self._name=newName
        return newName
    def getAddress (self):
        return self._address
    def setAddress(self,newAddress):
        self._address=newAddress
        return self._address
    def __del__(self):
        print('i have been deleted')


class Employee(Person):
    
    def __init__(self ,employeeNumber,name,address,salary,jobTitle,loans):
        self.employeeNumber=employeeNumber
        self.__salary=salary
        self.__jobTitle=jobTitle
        self.__loans=loans
        super().__init__(name,address)
    def getSalary(self):
        return self.__salary
    def getJobTitle (self):
        return self.__jobTitle
    def setJobTitle (self,newJob):
        self.__jobTitle=newJob
        return self.__jobTitle
    def getTotalLoans(self):
        
        return sum(list(self.__loans))
    def getMaxLon (self):
        return max(list(self.__loans))
    def getMinLon(self):
        return min(list(self.__loans))
    def getLoans (self):
        return self.__loans
    def setLoans (self,newLoans):
        self.__loans=newLoans
        return self.__loans
    def printInfo(self):
        
        print("Employee Number:", self.employeeNumber)
        print("Name :", self._name)
        print("Address :", self._address)
        print("Job Title :", self.__jobTitle)
        print("Salary :", self.__salary)
        
        print("Total Loans :", self.getTotalLoans())
    
        
      
      
      
class Student(Person):
   
    def __init__(self,studentNumber,name,address,subject,marks):
        self.studentNumber=studentNumber
        self.__subject=subject
        self.__marks=marks
        super().__init__(name,address)
    def getSubject(self):
        return self.__subject
    def setSubject (self,newSubject):
        self.__subject=newSubject
        return self.__subject
            
    def getMarks(self):
        return self.__marks
    def setMarks(self,newMarks):
        self.__marks=newMarks
        return self.__marks
    
    def getAverage (self):
        
     return sum(self.__marks.values())/len(self.__marks.values())
     
            
    def getAmarks(self):
        
       A = list(filter(lambda x: x>= 90, self.__marks.values()))
       return A 
   
    def printInfo (self):
        
        print("Student Number:", self.studentNumber)
        print("Name :", self._name)
        print("Address :", self._address)
        print("Subject :", self.__subject)
        print("Student's Average:", self.getAverage())
    
        
        
        
        
Employee1=Employee(1000,"Ahmad Yazaan","Amman Jordan",500,"HR Consultant",[434,200,1020])
Employee2= Employee(2000,"Hala rana","Aqaba jordan", 750,"Manager",[150,3000,250])
Employee3= Employee(3000,"Mariam ali","Mafraq jordan", 600,"HR s",[304,1000,250,300,500,235])
Employee4= Employee(4000,"Yasmin mohameed","Karak jordan", 865,"Director",[])
Student1=Student(20191000,"Khalid Ali","Irbid Jordan", "History",{"English":80,"Arabic":90,"Management":75,"Calculus":85, "OS":73,"Priogramming":91})
Student2=Student(20182000,"Reem Hani","Zarqa Jordan", "Softwere Eng",{"English":80,"Arabic":90,"Management":75,"Calculus":85, "OS":73,"Priogramming":90})
Student3=Student(20161001,"Nawras Abdallah","Amman Jordan", "Arts",{"English":83,"Arabic":92,"Art":90,"Management":75})
Student4=Student(20172030,"Amal Raed","Tafelah Jordan", "Computer Eng",{"English":83,"Arabic":92,"Management":70,"Calculus":80, "OS":79,"Priogramming":91})
 
employeeList=[]
employeeList.append(Employee1)
employeeList.append(Employee2)
employeeList.append(Employee3)


studentList=[]
studentList.append(Student1)
studentList.append(Student2)
studentList.append(Student3)
studentList.append(Student4)




 
for x in employeeList:
     print (x.getTotalLoans(),x.printInfo())
for x in studentList:
     print (x.printInfo(),x.getAverage())
avr=[]
for x in studentList:
    
    avr.append(x.getAverage())
print (max(avr)) 

maxLoan=[]
for x in employeeList:
    
    maxLoan.append(x.getMaxLon())
print (functools.reduce(lambda a,b : a if a > b else b,maxLoan)) 


minLoan=[]  

for x in employeeList:
    
    minLoan.append(x.getMinLon()) 

print (functools.reduce(lambda a,b : a if a < b else b,minLoan)) 


employeeLoans=[]
for x in employeeList:
    
    employeeLoans.append(x.getLoans())
print (employeeLoans)

totalLoan=[]
for x in employeeList:
    
    totalLoan.append(x.getTotalLoans())
print (totalLoan)

print (functools.reduce(lambda a,b : a+b ,totalLoan))

hsalary=[]

for x in employeeList:
    hsalary.append(x.getSalary())
    
print (functools.reduce(lambda a,b : a if a > b else b,hsalary))    


for x in employeeList:
    hsalary.append(x.getSalary())
print (functools.reduce(lambda a,b : a if a < b else b,hsalary))

print (functools.reduce(lambda a,b : a+b ,hsalary))

dictionery = {}
def LoanDict(listt):
   
    for x in listt:
        dictionery[x.getName()] = x.getLoans()
    print(dictionery)
LoanDict(employeeList)

print (functools.reduce(lambda a,b : a if a > b else b ,dictionery.values()))

dictionery1 = {}
def LoanDict(listt):
   
    for x in listt:
        dictionery1[x.getName()] = x.getLoans()
    print(dictionery)
LoanDict(employeeList)




    
    
     
      
        
    



