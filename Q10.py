#sort a list of tuples based on second element using lambda function

marks = [("physics", 88), ("chemistry", 92), ("maths", 90)]
print(marks)

print("Sorting on the basis of marks : ")

print("in ascending order")
marks.sort(key=lambda x : x[1])
print(marks)

print("in descending order")
marks.sort(key=lambda x : x[1], reverse = True)
print(marks)