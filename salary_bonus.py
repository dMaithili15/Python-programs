sal = int(input("Enter your salary : "))
yr = int(input("Enter the no of years you worked : "))
if yr>5:
    bonus=0.05*sal
    sal=bonus+sal
    print('Your bonus salary for this month is : ',sal)
else:
    print('Sorry,You are not eligible for bonus!!')   