#list --mutable(can change)

marks = [56, 98, 78, 44, 79]
print(marks[0])
print(marks[4])
print(len(marks))
print(type(marks))
print(marks)

marks[0] = 99
print(marks)

student = ["priya", 20, 98.4] #can be collection of different datatypes
print(student)

#print(student[4]) 
#error

#slicing
print(marks[1:4])
print(marks[:len(marks)])
print(marks[-4:])

list = [3, 1, 5, 2, 4]
print(list)
print(list.append(6)) #return none but add element in the end
print(list.sort()) #return none but sort
print(list)
print(list.sort(reverse = True))
print(list)

fruits = ["orange", "watermelon", "apple", "banana"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.insert(1, "mango")
print(fruits)

fruits.remove("watermelon")
print(fruits)
fruits.pop(0)
print(fruits)
