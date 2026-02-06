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

