file_name ="example.txt"
with open(file_name,"w+") as file:
    file.write("hello\n")
    file.write("world\n")
    file.seek(0)
    content = file.read()
    print(content)
with open(file_name,"r") as file:
    print(file.read())

file_name = "example.txt"
with open(file_name,"r+") as file:
    print(file.read())
    file.seek(0)
    file.write("updated content")
    file.seek(0)
    print(file.read())
with open(file_name,"r") as file:
    print(file.read()) 


with open(file_name,"a+") as file:
    file.write("\nThis is \n")
    print("updated content")
    file.seek(0)
    print(file.read()) 


file_name = "example.txt"
with open(file_name,"w") as file:
    file.write("hello\n")
    file.write("world\n") 
    file.write("india\n")
    file.seek(0)
with open(file_name,"r") as file:
    file.seek(0)
    content = file.read()
    print(content) 


#readlines
file_name="example2.txt"
with open(file_name,"w") as file:
    file.write("hello\n")
    file.write("world\n")
with open(file_name,"r") as file:
    content = file.readline()
    print(content)   
    content = file.readline()
    print(content)

#readlines
file_name = "example2.txt"
with open(file_name,"w") as file:
    file.write("I am ")
    file.write("Iron Man")
with open(file_name,"r") as file:
    content = file.readlines()
    print(content)    

#write(), writelines()
file_name = "example3.txt"
with open(file_name,"w") as file:
    file.write("this is write fn\n")
with open(file_name,"a") as file:
    line=["Hello","World"]
    file.writelines(line) 
with open(file_name,"r") as file:
    content = file.read()
    print(content) 


file_name ="example3.txt"
list=[]
with open(file_name,"r") as file:
    for i in file:
        list.append(i.strip())
print(list)   

file_name ="example3.txt"
with open(file_name,"r") as file:
    content = file.read()
print(content)   


file_name ="example4.txt"
with open(file_name,"w") as file:
    file.write("hello ")
    file.write("world ")
    file.write("team.\n")
k=""
with open(file_name,"r") as file:
    for line in file:
        k = k+ line
print(k)  

n = int(input("enter the value of n: "))
with open(file_name,"r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())  
file_name ="example3.txt"
n = int(input("enter value:"))
with open(file_name,"r") as file:
    lines =file.readlines()
    last=lines[-n:]

    for line in last:
        print(line.strip())

file_name = "example5.txt"
with open(file_name,"w") as file:
    file.write("Hello student today is holiday")
    longest_word =""
with open(file_name,"r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word        
print(longest_word)  

file_name="example6.txt"
with open(file_name,"w") as file:
    file.write("hello 123 today 23 is 78")
with open(file_name,"r") as file:    
    data = file.read()
word = data.split()
for i in word:
    if i.isdigit():
        print(i)

           




    
                     