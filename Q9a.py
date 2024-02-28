#PERMUTATION using build in function
import itertools

list1 = [1, 2, 3]
print("All Possible permutations are : ")
perm = list(itertools.permutations(list1))
print(perm)

p1 = list(itertools.permutations(list1, 2))
print(p1)