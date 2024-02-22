#classes in python
class Car:
    color = "red"
    year = 2024

c1 = Car()     #object
print(c1.color)
print(c1.year)

class Student:
    def __init__(self, name, section):     #constructor  -- default & parameterized
        self.name = name
        self.sec = section
        print("Constructor called !!")

    def __str__(self):  #tells how object will be printed
        return f"{self.name}({self.sec})"   
    
    def hello(self):    #user made methods
        print("Hello,", self.name) 

s1 = Student("Karan", "a")
print(s1.name)
print(s1.sec)
print(s1)
s1.hello()
s2 = Student("Priya","c")
print(s2)

del s2.sec
del s2
#print(s2)
#error as it is deleted now