lst = [10,10, 20, 30]
lst.append(40)
print( lst)

count = lst.count(10)
print( count)

index = lst.index(30)
print ( index)

print( lst.index(20))

# pop remove value from specific index
print( lst.pop(3))
print ( lst)

# clear remove all element from list
lst.clear()
print( lst)

numbers = [10,45,67,87,92]
numbers.remove(10)
print (numbers)
