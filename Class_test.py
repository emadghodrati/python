"""
Created on Thu Jan  3 16:32:48 2019

@author: Emad
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
#        print("Hello my name is " + self.name)
        print("Hello my name is {0} and I am {1} years old ".
              format(self.name,self.age))

p1 = Person("John", 36)
p1.age = 40
p1.myfunc()
del p1.age

try: 
    print(p1.age)
except Exception as e:
    print("We caught an error:",e)