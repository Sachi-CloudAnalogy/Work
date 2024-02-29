# 3: Implement a Python script to find and replace a specific string in a text file.

search = input("What you want to replace : ")
new_word = input("Replace it with : ")

with open("data for file.txt", "r") as f:
    data = f.read()
    data = data.replace(search, new_word)

with open("data for file.txt", "w") as f: 
    f.write(data)  
