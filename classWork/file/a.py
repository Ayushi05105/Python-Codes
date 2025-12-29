file_name = "example.txt"
with open(file_name,"a+") as file:
    file.write("This is\n")
    print("\n Updated file content:")
    file.seek(0)
    print(file.read())