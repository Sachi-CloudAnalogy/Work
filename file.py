#File IO

f = open("data.txt", "r")  #open file
txt = f.read()       #read file
print(txt)
print(type(txt))
f.close()      #close file

f2 = open("data.txt", "r")
t1 = f2.read(10)   #no of character to read
print(t1) 

line1 = f2.readline()  #read \n(next line) also
print(line1)

line2 = f2.readline()
print(line2)

line3 = f2.readline()   #print empty line as there is nothing left
print(line3)

f2.close() 


#with
with open("sample.txt","r") as f:
    t2 = f.read()
    print(t2)

with open("sample.txt", "w") as f:
    f.write("Hello world!!")

#to delete file import os module
import os    
os.remove("new.txt")   