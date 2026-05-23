# Check whether a number is prime.

num = int(input("enter the number :"))
if num<=1:
    print(num,'is not prime')
    
else:
    is_prime = True
    for i in range(2, num):
        if num%i==0:
            is_prime = False
            break
    
    
    if is_prime:
        print(num,'is prime')
        
    else:
        print(num,'is not prime')
            