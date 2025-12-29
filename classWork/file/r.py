file_name = "example.txt"
with open(file_name,"w") as file:
    file.write("This is the original content\n")
with open(file_name,"r+") as file:
    print("Original file content:")
    print(file.read())
    file.seek(0)
    file.write("Updated content\n")
    file.seek(0)
    print("\n update file content")
    print(file.read())
with open(file_name,"r") as file:
    print("\n Verified content from the file") 
    print(file.read())       