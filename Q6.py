#find all unique triplet in an array that sum upto a given target value

arr = [1, 2, 3, 4, 7, 8]
n = len(arr)
target = int(input("Enter target value : "))

def find(arr, n, target):
    #sorting the array
    arr.sort()
    for i in range(0,(n-2)):
            last = n-1    #last element
            next = i+1    #2nd element
            while(next < last):
                if arr[i] + arr[next] +arr[last] == target:
                    print(f"{arr[i]},{arr[next]},{arr[last]}")
                    next += 1
                elif arr[i] + arr[next] +arr[last] > target: 
                    last -= 1
                elif arr[i] + arr[next] +arr[last] < target:
                    next += 1        
    return -1

find(arr, n, target)


#time complexity = O(n2) 