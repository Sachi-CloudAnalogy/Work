list = [2, 4, 6, 8]  #iterable  -- contain iter() func
it = iter(list)      #iterator -- contain iter() & next() func

while True:
    try:
        print(next(it))
    except:
        break
    
print("List ended")        

def myloop(val):    #creating loop
    i = iter(val)
    while True:
        try:
            print(next(i))
        except StopIteration:
            break

myloop([2, 5, 8])
        