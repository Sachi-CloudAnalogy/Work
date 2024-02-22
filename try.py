#Exception handling in python

try:
    print(x)  #error
except:
    print("Error Occured")
finally:
    print("Everytime executed")      

try:
    print("Hello")
except:
    print("Error")
else:
    print("No Error")         

# you can raise exception in certain conditions
a = int(input("Enter Number ="))
if a < 0:
    raise Exception("Negative number not allowed")    
       