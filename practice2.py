# start with empty dictionary & add 3 values
marks = {}

x = int(input("enter phy marks : "))
marks.update({"phy" : x})

x = int(input("enter chem marks : "))
marks.update({"chem" : x})

x = int(input("enter math marks : "))
marks.update({"math" : x})

print(marks)