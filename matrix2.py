row = int(input("No of rows = "))
col = int(input("No of columns = "))

mat1 = []
print("Enter values of matrix 1 rowwise : ")
for r in range(row):
    a = []
    for c in range(col):
        a.append(int(input()))
    mat1.append(a)

for r in range(row):
    for c in range(col):
        print(mat1[r][c], end = " ")
    print()   

mat2 = []
print("Enter values of matrix 2 rowwise : ")
for r in range(row):
    a = []
    for c in range(col):
        a.append(int(input()))
    mat2.append(a)

for r in range(row):
    for c in range(col):
        print(mat2[r][c], end = " ")
    print()          

#RESULT
matrix = []    
for r in range(row):
    m = []
    for c in range(col):
        m.append(mat1[r][c] + mat2[r][c])
    matrix.append(m)

for r in range(row):
    for c in range(col):
        print(matrix[r][c], end = " ")
    print() 