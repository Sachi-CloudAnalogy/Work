# 1: Write a Python program to count the number of lines, words, and characters in a text file.

lines = 0
words = 0
char = 0
with open("Ques.txt", "r") as f:      #with will automatically detect EOF and stop and close file
    for line in f:
        lines += 1
        words += len(line.split())
        for i in line:
           if i != " " and i != "\n":    
            char += 1
        

print("No. of lines = ", lines)
print("No. of words = ", words)
print("No. of char = ", char)        
