#Python program to find reverse of any number
n=int(input("Enter any number : "))

n1=n%10
n=n//10
n2=n%10
n=n//10
rev=n1*100+n2*10+n
print("Reverse of number : ",rev )
