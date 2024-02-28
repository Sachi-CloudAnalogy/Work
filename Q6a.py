#find all unique triplet in an array that sum upto a given target value

arr = [1, 2, 3, 4, 7, 8]
n = len(arr)
target = int(input("Enter target value : "))

for i in range(0, (n-2)):    
    for j in range(i+1, (n-1)):
        for k in range(j+1, n):
            if (arr[i] + arr[j] + arr[k]) == target:
                print(f"[{arr[i]}, {arr[j]}, {arr[k]}]")
    
    
#time complexity = O(n3)    
