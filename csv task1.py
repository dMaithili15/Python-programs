import csv
f = open("Student.csv","w")
a = csv.writer(f)
a.writerow(["Name","Rollno","Mobileno","Emailid","Address"])
print(".............................................................")
Name = input("Enter Your Name: ")
Rollno = int(input("Enter Your Rollno: "))
Mobileno = int(input("Enter Your Contact no: "))
Address = input("Enter Home Address: ")
print(".............................................................")
p1=int(input("Enter 1st paper marks: "))
p2=int(input("Enter 2nd paper marks: "))
p3=int(input("Enter 3rd paper marks: "))
p4=int(input("Enter 4th paper marks: "))
p5=int(input("Enter 5th paper marks: "))
print(".............................................................")
total=p1+p2+p3+p4+p5
percent=total/5

print("Your data has been recorded Successfully!!!")
print(".............................................................")
f.close()