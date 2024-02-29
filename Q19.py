#Create a Python program to sort the lines of a text file alphabetically and write the sorted content back to the file

with open("ques2.txt", "r") as f:
    file = f.readlines()   #return a list of each line in file as list items
    print(file)
    
    file.sort()           #to sort it alphabetically
    print(file)

with open("ques2.txt", "w") as f:
        f.writelines(file)     #writelines() take any iterable as an argument
