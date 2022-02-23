a=int(input('Enter first number : '))
b=int(input('Enter second number : '))
c=int(input('Enter third number : '))
if a>b:
    if a<c:
        median=a
    elif b>c:
        median=b
    else:
        median=c
else:
    if a>c:
        median=a
    elif b<c:
        median=b
    else:
        median=c
    print('The Median among 3 number is : ',median)


   