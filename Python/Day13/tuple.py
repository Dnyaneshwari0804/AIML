#--------------Tuples--------------

# a tuple is an immutable data type in python
a=(1,23,23,45,"Rohan")
print(type(a))
# a tuple cannot be changed
no = a.count(23)
print(no) #returns the total no of values

i = a.index(45)
print(i)

print(a[1:2])
