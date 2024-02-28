#intersection of 2 sets

s1 = {1, 2, 3, 4, 5}
s2 = {2, 4, 6, 8, 10}

def intersect(s1, s2):
    return (s1 & s2)   #intersection

def union(s1, s2):
    return (s1 | s2)   #union

print("Intersection = ", intersect(s1, s2))
print("Union = ", union(s1, s2))
