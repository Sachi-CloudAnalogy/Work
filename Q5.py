#matrix [using list of lists]

matrix1 = [[1, 2, 1], [2, 1, 1]]     #2*3 size
print(matrix1)
matrix2 = []
row = int(input("No of rows = "))
col = int(input("No of columns = "))
print("Enter values rowwise :")
 
#taking values from user 
for r in range(row):
    mat = []
    for c in range(col):
        mat.append(int(input()))
    matrix2.append(mat)    

#printing matrix
for r in range(row):
    for c in range(col):
        print(matrix2[r][c], end = " ")    
    print()    