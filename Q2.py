#A company decided to give bonus of 1000Rs to employee if his/her services is more than 5 years 
# Ask user their salary and year of service and print the net bonus amount


salary = float(input("user salary:"))
years = int(input("year of service:"))

if years>5:
    print("his net salary is", salary+1000)

else:
    print("not applicable for bonous")   
