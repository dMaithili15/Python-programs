a=int(input('Enter number of classes held : '))
b=int(input('Enter number of classes attended : '))

per=(a/b)*100

if per>=75:
    print("You are allowed for Exam.")
else:
    print("You are not allowed for Exam.")