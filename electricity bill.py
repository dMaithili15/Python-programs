i = int(input("Enter the number of units consumed in a month : "))

if i<=50:
    bill=i*2.5+0.36
    print("Total bill amount for this month is : ",bill)
elif 50<i<=150:
    bill=i*5.5+0.36
    print("Total bill amount for this month is : ",bill)
elif 150<i<=300:
    bill=i*7.5+0.36
    print("Total bill amount for this month is : ",bill)
elif 300<i<=500:
    bill=i*10+0.36
    print("Total bill amount for this month is : ",bill)
else:
    bill=i*15+0.36
    print("Total bill amount for this month is : ",bill)

         