#how to find the sum of the numbers
print("Hello Kamba")
print("Fidning out the last digit and sun of the digits of the same number")
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
    
print("The total sum of digits is:",tot)



  
