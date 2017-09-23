a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
if (n==1):
    print("Enter a value greater than 1")
elif(n==0):
    print("Enter a value greater than 0")
else:
 while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
