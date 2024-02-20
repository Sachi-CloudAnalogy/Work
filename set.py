#set -- mutable
#elements of set -- immutable & unique (list and dict cannot be elements of set)
#unordered elements-- no index

collection = {1, 2, 3, 4, 5}
print(collection)
print(type(collection))

set1 = {"hello", "hi", 2, 4, 6, 4, 4}
print(set1)
print(len(set1))

empty_set = set() 
print(type(empty_set))
emp = {} #empty dictionary
print(type(emp))

set1.add(3)  #cant add list or dict
print(set1)  #can add tuple

set1.remove("hi")
print(set1)

set1.remove(4)
print(set1)

set1.clear()  #empties the set
print(set1)

print(collection.pop())  # gives any random value from set
print(collection.pop())

set2 = {3, 6, 9}
set3 = (2, 4, 6)

print(set2.union(set3))
print(set2.intersection(set3))

values = {2, 2.0}  #hash value of 2 & 2.0 is same 
print(values)  #2 only

values1 = {2, "2.0"}
print(values1)
