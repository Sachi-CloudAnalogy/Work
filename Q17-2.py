# 2: Create a Python program to merge multiple text files into a single file.

file_names = ['text1.txt', 'text2.txt']     #files to merge

with open("text3.txt", "a") as f1:      #merge all into this file
    for file in file_names:
        with open(file, "r") as f2:
            data = f2.read()
            f1.write(data)
