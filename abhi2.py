# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:38:18 2022

@author: hp
"""

class Person():
    def __init__(self,name):
        self.name=name
    def talk(self):
        print('lets talk')


name=input("write your name ")
person=Person(name)
person.talk()
print(person.name)
