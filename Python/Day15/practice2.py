m1 = int(input("Enter marks 1:"))
m2 = int(input("Enter marks 2:"))
m3 = int(input("Enter marks 3:"))

#check for total percentage

t_per = (100*(m1+ m2+ m3))/300

if(t_per>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are pass",t_per)

else:
    print("You, failed tryy next yearrr!!!!!!!!",t_per)