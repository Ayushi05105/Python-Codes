with open("Second.txt","a+") as f:
    f.seek(0)
    c =0
    s=0
    for line in f:
        #line = line.strip()
        #if line.isdigit():
            s+= int(line)
            c+=1
    result =f"\nSum:{s},count:{c}"
    f.write(result)

   

    