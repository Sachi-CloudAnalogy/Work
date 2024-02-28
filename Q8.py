#merge dictionary

dict1 = {"name" : "Priya",
         "course" : "MCA",
         "city" : "Delhi"}

dict2 = {"gender" : "female",
         "city" : "Agra",
         "company" : "CA"}

dict1.update(dict2)  #update common values also
print(dict1)