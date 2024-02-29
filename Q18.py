# Write a Python program to read a CSV file and convert its contents into a list of dictionaries.
import csv

with open("csv18.csv", 'r') as f:
    csv_file = csv.DictReader(f)   #read file in form of a dictionary
    list = []

    for i in csv_file:
        list.append(i)

#print
print(list)     
for i in list:
    print(i)
