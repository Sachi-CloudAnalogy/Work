#Recursion

#function of factorial
def fact(n):
    if(n == 1):
        return 1
    fac = n * fact(n-1)
    return fac

print("Factorial =", fact(5))

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(6)

#sum of first n natural numbers
def sum(n):
    if(n == 1):
        return 1
    return n + sum(n-1)

print("Sum =", sum(5))

#func to print all elements of a list
list = [2, 4, 6, 8, 0]

def travel(list, i):
    if(i == len(list)):
        return
    print(list[i])
    return travel(list, i+1)

print("List")
travel(list, 0)
