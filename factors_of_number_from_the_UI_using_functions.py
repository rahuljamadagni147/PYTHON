def factors_of_a_number(num):
   print("the factors of " ,num, "are :")
   for i in range (1, num+1):
     if (num%i==0):
       print(i)
 
# Let a be any variable that is the input taken by the user
a = int(input("enter the number to get the factors"))

factors_of_a_number(a)
