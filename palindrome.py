# check if a list is palindrome or not
list = [4, 2, 1, 4]

list2 = list.copy()
list2.reverse()
print(list2)

if(list == list2):
    print("Palindrome")
else:
    print("Not palindrome")    