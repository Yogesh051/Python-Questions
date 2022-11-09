x=int(input("side 1:"))
y=int(input("side 2:"))
z=int(input("side 3:"))

if (x+y>z):
    print("it will form a triangle")
elif(y+z>x):
    print("it will form a triangle")
elif(x+z>y):
    print("it will form a triangle")
else:
    print("not possible to form a triangle")
