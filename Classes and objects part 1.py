# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 18:23:04 2021

@author: mon pc
"""


class Pupil:#creating a new class called for an object called Pupil
    def __init__(self, name, age, Class): # defining the various attributes of the object which are the name, age and class
        self.name = name
        self.age = age #assigning name, age and class to a single entity known as self in these 3 lines of code
        self.Class = Class
        
    def present_self(self):
        print("My name is " , self.name)
        print("I am " , self.age , "years old")
        print("I am in class" , self.Class)
p1 = Pupil('Mary Peters', 10, 6)
p2 = Pupil("John Rice", 11, 6 )

p1.present_self()
p2.present_self()


