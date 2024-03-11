# Create a Python program to perform matrix multiplication using operator overloading.

n = 3      #dimension of matrix = n*n

class Matrix:
    def __init__(self):
        self.arr = [[0 for i in range(n)]for j in range(n)]

    def input(self, A):
        for i in range(n):
            for j in range(n):
                self.arr[i][j] = A[i][j]

    #operator overloading
    def __mul__(self, x): 
        mat = [[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = 0
                for k in range(n):
                    mat[i][j] += self.arr[i][k] * x.arr[k][j]
        #printing            
        for i in range(n):
            for j in range(n):
                print(mat[i][j], end = " ")
            print()           

arr1 = [[1, 2, 3], 
        [4, 5, 2], 
        [7, 3, 1]]
arr2 = [[7, 8, 9], 
        [1, 2, 3], 
        [4, 1, 2]]   

mat1 = Matrix()
mat2 = Matrix()
mat1.input(arr1)
mat2.input(arr2)

print("multiplication of 2 matrix : ")
mat1 * mat2