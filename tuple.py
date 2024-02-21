#tuple -- immutable

tup = (3, 5, 2, 9, 3)
print(tup)
print(type(tup))
print(tup[2])

#tup[1] = 4  (immutable)
#error

tup2 = ()  #empty tuple
tup3 = (1,)  #single element tuple
tup4 = (1)  # will take it as int
tup5 = (1.0) # will take as float
tup6 = ("hi") #will take as str
# comma is a must for single element tuple

print(tup2)
print(type(tup2))
print(tup3)
print(type(tup3))
print(tup4)
print(type(tup4))
print(type(tup5))
print(type(tup6))

print(tup[1:3])

print(tup.index(9))
print(tup.count(3))

#delete complete tuple
del tup
#print(tup)  will give error
#as it doesnt exist now
