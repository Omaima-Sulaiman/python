#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:56:50 2019

@author: omaima
"""
from tkinter import *
from tkinter import messagebox
from functools import reduce
class Person:
    def __init__(self, name, address):
        self._name = name
        self._address = address
    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name
    def getAddress(self):
        return self._address
    def setAddress(self, address):
        self._address = address
    def __del__(self):
        print(f'Student {self._name} has been deleted')
class Employee(Person):
    def __init__(self, employee_number, name, gender, nationality, dob, address, department, salary):
        super().__init__(name, address)
        self.employee_number = employee_number
        self.__gender = gender
        self.__nationality = nationality
        self.__dob = dob
        self.__department = department
        self.__salary = salary
    def getEmployeeNumber(self):
        return self.__employee_number
    def setEmployeeNumber(self, employee_number):
        self.__employee_number = employee_number
    def getGender(self):
        return self.__gender
    def setGender(self, gender):
        self.__gender = gender
    def getNationality(self):
        return self.__nationality
    def setNationality(self, nationality):
        self.__nationality = nationality
    def getDob(self):
        return self.__dob
    def setDob(self, dob):
        self.__dob = dob
    def getDepartment(self):
        return self.__department
    def setDepartment(self, department):
        self.__department = department
    def getSalary(self):
        return self.__salary
    def setSalary(self, salary):
        self.__salary = salary
    def printInfo(self):
        print(f'''
       Name: {self._name}
       Address: {self._address}
       Employee Number: {self.employee_number}
       Salary: {self.__salary}
       Gender: {self.__gender}
       Nationality: {self.__nationality}
       Date of birth: {self.__dob}
       Department: {self.__department}
        ''')
    def __del__(self):
        print(f'Employee: {self.employee_number} have been deleted')
employees_list = []
root = Tk(className="My First GUI")
root.geometry('500x500+500+100')
top = Menu(root)
root.config(menu=top)
def add_employee():
    c = Toplevel(root)
    c.title("Add New Employee")
    c.geometry("500x500+510+230")
    Label(c, text="Add New Employee").grid()
    employee_number = Label(c, text="Employee Number").place(x=20, y=20)
    name = Label(c, text="Name").place(x=20, y=40)
    gender = Label(c, text="Gender").place(x=20, y=60)
    nationality = Label(c, text="Nationality").place(x=20, y=80)
    dob = Label(c, text="Date of birth").place(x=20, y=100)
    address = Label(c, text="Address").place(x=20, y=120)
    department = Label(c, text="Department").place(x=20, y=140)
    salary = Label(c, text="Salary").place(x=20, y=160)
    employee_number_value = IntVar()
    name_value = StringVar()
    gender_value = StringVar()
    nationality_value = StringVar()
    dob_value = StringVar()
    address_value = StringVar()
    department_value = StringVar()
    salary_value = IntVar()
    e1 = Entry(c, textvariable=employee_number_value).place(x=150, y=20)
    e2 = Entry(c, textvariable=name_value).place(x=150, y=40)
    e3 = Entry(c, textvariable=gender_value).place(x=150, y=60)
    e4 = Entry(c, textvariable=nationality_value).place(x=150, y=80)
    e5 = Entry(c, textvariable=dob_value).place(x=150, y=100)
    e6 = Entry(c, textvariable=address_value).place(x=150, y=120)
    e7 = Entry(c, textvariable=department_value).place(x=150, y=140)
    e8 = Entry(c, textvariable=salary_value).place(x=150, y=160)
    def save_employee():
        employee = Employee(
            employee_number_value.get(),
            name_value.get(),
            gender_value.get(),
            nationality_value.get(),
            dob_value.get(),
            address_value.get(),
            department_value.get(),
            salary_value.get()
        )
        employee.printInfo()
        employees_list.append(employee)
    Button(c, text="Save", command=save_employee).place(x=30, y=200)
def view_employee():
    c = Toplevel(root)
    c.title("View Employee")
    c.geometry("500x500+510+230")
    Label(c, text="View Employee").grid()
    for employee in employees_list:
        data = f"Name: {employee.getName()} \t" \
               f"Address: {employee.getAddress()} \t" \
               f"Number: {employee.employee_number} \t" \
               f"Gender: {employee.getGender()} \t" \
               f"Salary: {employee.getSalary()} \t" \
               f"Nationality: {employee.getNationality()} \t" \
               f"Date of birth: {employee.getDob()} \t" \
               f"Department: {employee.getDepartment()} \t"
        Label(c, text=data).grid()
top = Menu(root)
root.config(menu=top)
file = Menu(top, tearoff=0)
file.add_command(label="Exit", command=root.destroy)
top.add_cascade(label="File", menu=file)
employees = Menu(top, tearoff=0)
employees.add_command(label='Add', command=add_employee)
employees.add_command(label='View', command=view_employee)
top.add_cascade(label="Employees", menu=employees)
root.mainloop()