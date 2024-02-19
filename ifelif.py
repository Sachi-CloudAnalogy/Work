#conditional statements
marks = int(input("enter marks : "))

if(marks < 33):
    print("fail")
elif(marks >= 33 and marks <=75):
    print("pass, average student")
elif(marks > 75 and marks <= 100):
    print("Good student")
else:
    print("invalid marks")            
