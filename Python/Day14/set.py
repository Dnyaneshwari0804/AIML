#set is a collection of non repetitive elements
#set is an unordered
# sets are uninedexed
# there is no way to changes items in set
# cannot contain duplicate values

s= set()
s.add(16)
s.add(56)
print(s)

#e= set() it will create an empty dict

s1= {1,2,3,4,6,7,"Dnyanu"}
print(s1)
print(type(s1))

# Methods
print(s.clear())
print(s1.remove(1))

#union

s2={1,2,45}
s3 ={2,4,5}
print(s2.union(s3))
print(s2.intersection(s3))
