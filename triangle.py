s1 = int(input("Enter First side of a triangle : "))
s2 = int(input("Enter Second side of a triangle : "))
s3 = int(input("Enter Third side of a triangle : "))

if s1==s2 and s1==s3:
    print("Given triangle is Equilateral.")
elif s1==s2 and s1!=s2:
    print("Given triangle is Isosceles.")
else:
    print("Given triangle is Scalene.")

