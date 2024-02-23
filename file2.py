#write in file

f = open("data2.txt", "w")   #delete everything then write
f.write("New Page !!!")   
f.close()

f = open("data2.txt","a")    #add data to existing file
f.write("\nWhat next ??")
f.close()

#create new file
f = open("new.txt", "w")
f.write("New file !!")
f.close()

f = open("sample.txt", "a")
f.write("Another new file !!")
f.close()
