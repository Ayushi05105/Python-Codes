file_name ="example.txt"
with open(file_name,"w") as file:
  file.write("Hello,this is a test using w+ mode.\n")
  file.write("This mode allows both writing and reading.\n")
  file.seek(0)
  content = file.read()
  print("File content after writing")
  print(content)
with open(file_name,"r") as file:
  print("Verified content from the file:")
  print(file.read())  
