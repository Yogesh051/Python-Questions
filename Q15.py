'''Write a program to print the following number patterns using a loop
a) 1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
   
b) 5 4 3 2 1
   4 3 2 1 
   3 2 1
   2 1
   1'''

n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()   
    
    

for i in range(5,0,-1):
    for j in range(0,i):
        print(5-j,end=" ")
    print()