# Implement a Python script to find the most frequently occurring word in a text file

word = ''
count = 0
words = []
maxCount = 0
with open("ques3.txt", "r") as f:
    for line in f:
        data = line.lower().replace(",", "").replace(".","").split()
        for i in data:
            words.append(i)

for i in range(len(words)):
    count = 1
    for j in range(i+1, len(words)):
        if words[i] == words[j]:
            count += 1
    if(count > maxCount):
        maxCount = count
        word = words[i]

print("Most Frequently occuring word = ", word, ",", maxCount)