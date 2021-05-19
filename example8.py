age1=int(input("enter the num"))
age2=int(input("enter the num"))
age3=int(input("enter the num"))
if age1>=age2 and age2>=age3:
    print("age1 is oldest")
elif age2>=age1 and age2>=age3:
    print("age2 is oldest")
elif age3>=age1 and age3>=age2:
    print("age3 is oldest")
else:
    print("age1,age2,age3 equal")