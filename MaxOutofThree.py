age1 = int(input("Enter age of First person"))
age2 = int(input("Enter age of Second person"))
age3 = int(input("Enter age of Third person"))

if (((age1>age2) and (age1>age3)) ) :
    print("first Person is Oldest with age {}".format(age1))
elif(((age2>age1) and (age2>age3)) ) :
    print("second Person is oldest with age {}".format(age2))
elif(((age3>age1) and (age3 > age2)) )  :
    print("Third Person is oldest with age {}".format(age3))
elif(age3==age2==age1):
    print("All are of same age")