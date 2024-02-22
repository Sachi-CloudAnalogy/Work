#class that take name and marks of 3 subjects as argument and method that give average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Avarage =", sum/3)    

     #static method -- that doesnt have self as argument
    @staticmethod   #decorator    
    def hello():
        print("Hello!!!")          

s1 = Student("Priya", [80,90,70])
print(s1.name)
print(s1.marks)
s1.avg()

s1.name = "Riya"  #can change value of attribute
print(s1.name)
s1.hello()

# __ make a method private -- not accessible outside class
