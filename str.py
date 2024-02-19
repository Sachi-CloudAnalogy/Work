#Strings  -- immutable(cant change)
str1 = "Hello"
str2 = "World"
final = str1 + " " + str2
print(final)
print(len(final))

str1 = "Hi"
print(str1)

print(str1[1])
#str1[1] = "y"
#modifing using index is not allowed

#slicing
print(str2[1:4])
print(str2[:len(str2)])

str = "python code"
print(str[-5:-2])

print(str.capitalize()) #make a new string and then make changes to it.
print(str)

print(str.replace("python", "Java")) #doesnt change original string
print(str)

print(str.find("code"))
print(str.find("H"))

print(str.count("o"))