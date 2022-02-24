a1=int(input('Enter the age of 1st person: '))
a2=int(input('Enter the age of 2nd person: '))
a3=int(input('Enter the age of 3rd person: '))
a4=int(input('Enter the age of 4th person: '))

if a2<a1>a3 and a1>a4:
    print("Oldest among 4 is: ",a1)
elif a1<a2>a3 and a2>a4:
    print("Oldest among 4 is: ",a2)
elif a1<a3>a2 and a3>a4:
    print("Oldest among 4 is: ",a3)
else :
    print("Oldest among 4 is: ",a4)

if a2>a1<a3 and a1<a4:
    print("Youngest among 4 is: ",a1)
elif a1>a2<a3 and a2<a4:
    print("Youngest among 4 is: ",a2)
elif a1>a3<a2 and a3<a4:
    print("Youngest among 4 is: ",a3)
else :
    print("Youngest among 4 is: ",a4)

