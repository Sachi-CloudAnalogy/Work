#different modes
#read and write

f = open("sample.txt", "r+")
f.write("Hello")  #in read mode, it overwrites
print(f.read())
f.close()

f = open("sample.txt", "w+")
print(f.read())  #empty
f.write("Hi !!!")
f.close()

f = open("sample.txt", "a+")
print(f.read())  #moves pointer to the end so it is also empty
f.write("\nHelloo !!!")
f.close()
