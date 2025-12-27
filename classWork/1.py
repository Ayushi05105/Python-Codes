from math import pow,sqrt
with open("f.txt","a+") as f:
    a = f.readline().split(',')
    s =0
    for i in a:
        if int(i)%2==0:
            s+=pow(int(i),2)
    print(s)        

