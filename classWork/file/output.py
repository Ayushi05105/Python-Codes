def count(s):
    for str in s.split():
        s="&".join(str)
        print(s)
print(count("python is fun to learn"))  

file_name ="ABC.txt"
with open(file_name,"w") as file:
    file.write("this is the 23 game")
line_count=0
word_count=0
char_count=0
with open(file_name,"r") as file:
    for line in file:
        line_count +=1
        word_count +=len(line.split())
        char_count +=len(line)
print(line_count)
print(word_count)
print(char_count)   

f1="ABC.txt"
f2="example6.txt"
with open(f1,"r") as file:
    content = file.read()
with open(f2,"w") as file1:
    file1.write(content)    
