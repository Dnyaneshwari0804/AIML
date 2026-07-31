#list are mutable
#list can be indexed just like a string
#can store any type of data

list1 =[False, "Rohit", "Apple",23,20.56]
print(list1[0])
list1[0]= "Grapes"
print(list1)
print(list1[1:4])
print(list1)

#list methods

list1.append("Dnyanu")
print(list1) #adds value at the end

l1=[1,2,3,45,6,7]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3,435) #insert 435 such that its index in the list 3
print(l1)
l1.pop(3) 
print(l1)
va = l1.pop(2)
print(va)
print(l1)
l1.remove(7)
print(l1)