matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

# 2nd
numbers = [5, 2, 6, 9, 12]
numbers.append(20)   # append => add back side of the list
numbers.insert(0,10) # insert => add on starting 0,10 means on 0th index add 10.
numbers.remove(5)
numbers.pop()        #remove 1st no. from starting
print(numbers)

#3rd
numbers = [5, 2, 6, 9, 12]
numbers.sort()
numbers.reverse()
numbers
print(numbers)

#4th
#print duplicate of list
numbers = [2, 3, 4, 2, 6, 1, 4, 3]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)        
