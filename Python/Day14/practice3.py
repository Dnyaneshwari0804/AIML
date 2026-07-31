s = set()
s.add(18)
s.add("18")
print(s)
#yes we can have a set with 18(int)
# and '18' (str) as a value in it
s1=set()
s1.add(20)
s1.add(20.0)
s1.add('20')
print(len(s1))

#if first no is same then python ignores the floating point

s3 = {}
print(type(s3))