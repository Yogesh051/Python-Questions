#program to find the attendance percentage of a student

attn = int(input("enter the lecture attended:"))
collegedays = int(input("total lecture:"))

attnpercent = (attn/collegedays)*100

if attnpercent>= 75:
    print("applicable for test")
    print("attendance percentage:", attnpercent )
else:
    print("not applicable for test")
    print("attendance percentage:",attnpercent)    