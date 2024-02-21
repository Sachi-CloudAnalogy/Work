list = ["delhi", "agra", "mumbai", "pune", "noida"]

def length(list):
    print(len(list))

length(list)    #print length of list

#print each element of list in single line
def ele(list):
    for i in list:
        print(i, end = " ")    #end = " " for printing in same line

ele(list)
print("\n")

print("hello" ,end = " ")
print("world")

print("hello", "hi", sep = " & ")  #sep defines what to come when divided by comma

#by default end = "\n"  and sep = " "


#func to convert USD to INR
def convert(usd):
    inr = usd * 83
    return inr

print("usd to inr =", convert(5))


# func for even odd
def find(num):
    if(num%2 == 0):
        print("Even")
    else:
        print("Odd")

find(7)
find(4)
