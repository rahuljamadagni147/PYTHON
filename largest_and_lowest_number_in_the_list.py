a=[]
n=int(input("Enter the number of elements: "))
for i in range(1, n+1):
 b=int(input("Enter element "))
 a.append(b)
a.sort()
print(a)
print("The largest element in the list is: " ,a[n-1])
print("The second largest element in the list is: " ,a[n-2])
print("the lowest number in the list is: ",a[n-n])
