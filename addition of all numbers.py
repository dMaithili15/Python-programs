num=int(input("Enter any value: "))

if num==0:
    print("Wrong Input...Please re-enter")
else:
    sum=int(num%10)+int(num/10)
    print(sum)
