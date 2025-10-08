a = [3,1,2,5,6]
sum = 0
for num in a:
    sum += num
print(sum)
print(sum/len(a))

arr = [5 ,6,7,8,9]
i = 0
j = len(arr) -1
while(i<j):
    arr[i],arr[j] = arr[j],arr[i]
    i+=1
    j-=1
    print(arr)

def linear_search(arr,target):
    i = 0
    while i <len(arr):
        if arr[i] == target:
            return i
        i +=1
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1        