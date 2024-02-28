import array

arr = array.array("i", [1, 2, 3, 4, 5])
n = len(arr)
print(arr)

k = int(input("no. of steps to rotate by :"))
k = k % n

#reversing the array
arr.reverse()

#splitting into 2 parts
arr1 = array.array("i", arr[0:k])
arr2 = array.array("i", arr[k:n])

#again reversing
arr1.reverse()
arr2.reverse()
#merging
arr1.extend(arr2)
print(arr1)
