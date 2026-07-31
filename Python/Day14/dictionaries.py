#---------Dictioanry-------
#IT is a collection of key value pairs
#it unordered, mutable, indexed, cannot contain duplicate keys

dict1={
    "Dnyanu":100,
     "ram":12,
      "sita":10
}
print(dict1, type(dict1))
print(dict1["Dnyanu"])

#Methods

print(dict1.items())
print(dict1.keys())
print(dict1.values())
dict1.update({"Dnyanu":99})
print(dict1)

print(dict1.get("ram")) #print none
print(dict1["ram"]) #returns an error

print(dict1.pop("ram"))