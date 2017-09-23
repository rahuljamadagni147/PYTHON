a=[]
odd=[]
even=[]
n=int(input("Enter the number of elements: "))
for i in range(1, n+1):
  b=int(input("Enter element "))
  a.append(b)
  a.sort()
  if(b%2==0):
   even.append(b)
  else:
   odd.append(b)
  print(a)

print("The list with even elements is: ",even)
print("The list with odd elements is: ",odd)
print("the largest even number in the list is: ",even[n-4])
print("the largest odd number in the list is: ",odd[n-4])

