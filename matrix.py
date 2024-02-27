#adding 2 matrix

m1 = [[1, 2], [3, 4]]
m2 = [[1, 2], [3, 4]]
m3 = [[0, 0], [0, 0]]

for r in range(len(m1)):
    for c in range(len(m1[0])):
        m3[r][c] = m1[r][c] + m2[r][c]
print(m3)        



