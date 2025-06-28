message = input(">")
words = message.strip().split(' ')  #strip used for unwanted spaces or newlins
emojis ={
    ":)" :"😄",
    ":(" :"😒",
}
output =""
for word in words:
   output += emojis.get(word.strip(),word) + " "
print(output)   