#Rotate a given array by K steps
#RIGHT
arr = [1, 2, 3, 4, 5]   #in form of list
n = len(arr)
print(arr)
k = int(input("no. of steps you want to right rotate the array by :"))

def right_rotate(arr, n, k):
    k = k%n
    arr.reverse()

    a1 = []
    a1.extend(arr[0:k])
    a1.reverse()
   
    a2 = []
    a2.extend(arr[k:n])
    a2.reverse()

    new = []
    new.extend(a1)
    new.extend(a2)
    print(new)

right_rotate(arr, n, k)

arr = [1, 2, 3, 4, 5]   
n = len(arr)
print(arr)
k = int(input("no. of steps you want to left rotate the array by :"))

#LEFT
def left_rotate(arr, n, k):
    k = k%n
    arr.reverse()

    a1 = []
    a1.extend(arr[0:n-k])
    a1.reverse()
   
    a2 = []
    a2.extend(arr[n-k:n])
    a2.reverse()

    new = []
    new.extend(a1)
    new.extend(a2)
    print(new)

left_rotate(arr, n, k)
     