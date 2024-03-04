rno=int(input("Enter Roll Num :"))
sname=input("Enter Student Name :")
s1=int(input("Enter Marks of Subject 1 :"))
s2=int(input("Enter Marks of Subject 2 :"))
s3=int(input("Enter Marks of Subject 3 :"))

total=s1+s2+s3
per=total/3

print("Roll Number : ",rno)
print("Student Name : ",sname)
print("total Marks : ",total)
print("percentage :",per)

if per >= 70:
    print("Distinctaion")

elif per >= 60:
    print("First class")

elif per >= 50:
    print("Second class")

elif per >= 40:
    print("Pass")

else:
    print("Fail")