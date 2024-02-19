#nested dictionary

dict = {
    "name" : "Priya",
    "location" : "Delhi",
    "courses" : {
        "bca" : 2020,
        "mca" : 2022
    } 
}

print(dict.keys())
print(list(dict.keys()))

print(dict.values())
print(list(dict.values()))

print(dict)
print(dict.items())

print(dict.get("name"))
print(dict["name"])

dict.update({"working" : True})
print(dict)

dict["non"] = "yes"
print(dict)

new_dict = {"name" : "Rahul", "year" : 2024}  #duplicate keys not allowed
                                              #it only overwrite them
dict.update(new_dict)
print(dict)
