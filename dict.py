#Dictionary -- mutable, unordered(no index)

info = {
    "key" : "value",
    "date" : 19,
    "day" : "Monday",
    "year" : 2024,
    "working" : True
}
print(info)

#can store list and tuples in a dictionary
student = {
    "subjects" : ["math", "phy", "chem"],  #list
    "marks" : (78, 99, 92)    #tuple
}
print(student)

#dictionary keys can be int, float, tuple (anything that doesnt change)
#keys can not be list or dictionary as they are mutable.
print(type(info))

#can access values through key
print(info["day"])
print(info["year"])

#error  
#print(info["name"])  -- as this key doesnt exist

info["date"] = 20 #update
print(info)

#add key
info["name"] = "Sachi"
print(info)

empty = {}
print(empty)
empty["YN"] = True
print(empty)