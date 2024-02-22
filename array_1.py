#Arrays in python
import array as arr

val = arr.array("i", [1, 2, 3, 4, 5])
print(val)

print(val.buffer_info())  #gives size of array
print(val.typecode) # gives type

val.reverse()
print(val)

val.append(8)
print(val)

print(val[3])

for i in range(len(val)):
    print(val[i])

for j in val:
    print(j)
    
ar = arr.array("d", [2.4, 5.6, 7.8])
print(ar)

ar.insert(0, 9.9)
print(ar)
ar.append(1.1)
print(ar)

#slicing
print(ar[3:5])
