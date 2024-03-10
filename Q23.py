# Write a Python program to compare two text files and output the differences between them.

from difflib import Differ      #to compare files

with open("file23a.txt", "r") as f1, open("file23b.txt", "r") as f2:
    file1 = f1.readlines()
    file2 = f2.readlines() 
    differ = Differ()

    difference = differ.compare(file1, file2)
    print(difference)

    for line in difference:
        print(line)
       

# " - "  means not present in file2
# " + "  means not present in file1
# no symbol means common in both files        
              