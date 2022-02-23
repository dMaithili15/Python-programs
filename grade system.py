i=int(input("Enter marks obtained Out of 100 : "))

if i>80:
    print('Grade = A')
elif 60<i<80:
    print('Grade = B')
elif 50<i<60:
    print('Grade = C')
elif 45<i<50:
    print('Grade = D')
elif 25<i<45:
    print('Grade = E')
else:
    print('Grade = F')
