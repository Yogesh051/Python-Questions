'''Company will give bonus on following criteria'''

#Time spent in company                  Bonus
#    >10 years                           10%
#    >6 and <10                           8%
#    <6                                   5%

'''Ask the salary and time spent by the user
print the net bonus amount accoundingly'''

salary=int(input("salary of user is:"))
time_spent=int(input("num. of years spent in company:"))

if time_spent>10:
    bonus=(10/100)*salary
    print("his net salary is", salary+bonus)

elif time_spent>6 and time_spent<=10:
    bonus=(8/100)*salary
    print("his net salary is", salary+bonus)

elif time_spent<6:
    bonus=(5/100)*salary
    print("his net salary is", salary+bonus)
    
else:
    print("no bonus")