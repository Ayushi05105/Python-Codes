def Selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

    return arr; 
list =[6,8,2,9,7,0]
Selection_sort(list)
print("sorted array:" , list)
