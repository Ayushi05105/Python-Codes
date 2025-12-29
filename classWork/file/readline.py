file_name = "example.txt"
with open(file_name,"w") as file:
    file.write("Hello\n")
    file.write("World\n") 
    file.write("Python\n")    

with open(file_name,"r") as file:

#read---> read all content
    print("\n Using readline():")  
    content =file.read()
    print(content)

#readline----> it read line by line  
    print("\n Using readline():")  
    line = file.readline()
    print(line,end=" ")
   # line = file.readline()
   # print(line,end=" ")

#using readlines()---> converts it into list
    print("\n Using readlines():")
    lines = file.readlines()
    print(lines)