def Fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fibonacci(n-1) + Fibonacci(n-2))  

nterms = int(input("Enter the number? "))  
if nterms <= 0:  # check if the number is valid 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(FibRecursion(i))