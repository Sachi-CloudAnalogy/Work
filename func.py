#functions

def print_hi():
    print("Hi !!!")

print_hi()
print_hi()

output = print_hi()  # no output -- None
print(output)

def sum(a, b):
    sum = a+b
    return sum

print(sum(7, 9))