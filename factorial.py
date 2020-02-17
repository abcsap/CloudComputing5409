def factorial(num):
  if num < 0:
    print("Please enter positive numbers only.")
  elif num == 0:
   print("The factorial of 0 is 1.")  
  else:
   fact =1 
   for i in range(1,num+1):
       fact = fact*i
   print("The factorial of",num,"is",fact)

num = int(input("Enter the number : ")) 
factorial(num)
