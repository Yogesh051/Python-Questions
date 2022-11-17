'''create a function using following conditions 
it should accept employee name and salary and display both
if the salary is missing in the function then assign the default value 10000 to salary 
ben(9000) mike(15000) bob ()'''

def myfunc(name, salary=10000):
    print(name, salary)
myfunc("ben",9000)
myfunc("mike",15000)
myfunc("bob")