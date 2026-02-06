friends = [ "Atif","Mazhar", "Talha","shayan"]

print ( friends[0])

# unlike string lists are immutable ...
friends[0] = "Raza"
print ( friends[0])

# slicing in list 
# it print indext 1 to 2 strings 
print ( friends[ 1:3])

friends.append("Zalzala")
print ( friends)


l1 = [ 1,6,34,26,63,22]
l1.sort()
# insert 10000  into list at index 3 
l1.insert( 3, 10000)

# pop remove the index 
value = l1.pop(2)
print( value)
print( l1)


print( type(l1))
