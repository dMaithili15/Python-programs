list=[]
n=int(input(" Enter size of list : "))

for i in range(0,n):
        element=int(input(" Enter the elements of list : "))
        list.append(element)
if n%2!=0:
    print("Wrong Input..Please enter even number of elements.")
elif n%2==0:
    i=0
while i<n:
    add=list[i]+list[n-1]
    i+=1
    n-=1
    print("Sum : ",add)
    # if n%2!=0:
    #    print("Wrong Input..Please enter even number of elements.")
    # elif n%2==0:
    #      i=0
    #     while i<n:
    #     add=list[i]+list[n-1]
    #     i+=1
    #     n-=1
    #     print("Sum : ",add)