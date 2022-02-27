n=int(input("Enter the multiples of 3 or 5 : "))
for i in range(0,1):
    if n%3==0 and n%5!=0:
        print("Fizz")
    elif n%3!=0 and n%5==0:
        print("Buzz")
    elif n%3==0 and n%5==0:
        print("FizzBuzz")
    else:
        print("Wrong Input")
    
    
    
    
