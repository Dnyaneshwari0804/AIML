#string are immutable they can not be changed

a="Hhii!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Hhii" , "Dnyanu"))
print(a.split(" "))
head="introduction to python"
print(head.capitalize())

s1="hello"
print(len(s1))
print(len(s1.center(50)))
print(a.count("hii"))

s2= "console"
print(s2.endswith("!!!"))

s2= "console to"
print(s2.endswith("to",4,10))

s1 = "hii hello "
print(s1.find("ello"))
#print(s1.index("ello"))

s1= "welcomeToTheConsole"
print(s1.isalnum())

s1 = "welcome"
#print(s1.alpha())

s1="hii"
print(s1.islower())
s1="hii"
print(s1.isprintable())
s1="hii"
print(s1.istitle())
s1="python is easy to use"
print(s1.startswith("python"))
s1="hii"
print(s1.swapcase())
s1="hii"
print(s1.title())
