# "Write a Python script that reads a text file called ""input.txt"", counts the frequency of each word in the file,
# and then writes the results to a new text file called ""word_count.txt"" with each word and its frequency
# separated by a colon."

with open("input.txt", "r") as f1:
    d = dict()         #creates an empty dictionary
    for data in f1:
        data = data.strip().lower()
        words = data.split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1    


with open("word_count.txt", "w") as f2:
    for key in list(d.keys()):
        data = f"{key} : {d[key]} \n"
        f2.write(data)