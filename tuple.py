# we cannot change tuple like string 

a = ( 1,3,2,"atif","mazhar")
print(type(a))

# Tuple methods 
# count how much time value appear in tuple 
no = a.count(2)
print( no)

# return index
i = a.index( "atif")
print("The index of Atif is: ", i)

# length of tuple 
print( len(a))


b = ( 1,2,2,3,"atif", "mazhar")
print ( b)


index = b.index(2)
print( index)

count = b.count(2)
print( count)

# slicing on tuple 
print ( b[2:5])
print  ( 2 in b)
print ( "atif" in b)
print ( b[5])

# we can use logical operator on tuple 
print ( "mazhar" not in b)
print ( (2 and 5) in b)
print ( ("atif" or "shayan") in b)

# print all elements of tuple
print ( b[:])
# it will print last value in tuple 
print ( b[-1])

# it will print all value from reverse side
print ( b[-3:-1])
''' It print empty tuple because python goes forward 
 we are trying to start from index -1 which is last index and goes reverse
 but in python it goes forward so that is why it print empty tuple 
'''
print( b[-1:-3])
