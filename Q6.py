'''take input of age from three people determine oldest and youngest'''

age1 = int(input("age of first person:"))
age2 = int(input("age of second person:"))
age3 = int(input("age of third person:"))

if age1>age2>age3:
    print("first person is oldest")
    print("third person is youngest")

elif age1>age3>age2:
    print("first person is oldest")
    print("second person is youngest")

elif age3>age2>age1:
    print("third person is oldest")
    print("first person is youngest")

elif age3>age1>age2:
    print("third person is oldest")
    print("second person is youngest")    

elif age2>age1>age3:
    print("second person is oldest")
    print("third person is youngest") 

elif age2>age3>age1:
    print("second person is oldest")
    print("first person is youngest")     

elif age1==age2==age3:
    print("all are of same age")
