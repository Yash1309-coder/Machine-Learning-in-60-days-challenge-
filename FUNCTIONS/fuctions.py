number  = int(input("Enter a number to find its factorial"))
factorial = 1
if number == 0 :
    print( "the factorial of 0 is 1")
else :
    for i in range (1 , number+1):
        factorial = factorial*i
        print(factorial)
    
    
  