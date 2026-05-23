# Find factorial of a number 

num = int(input("enter number for find factorial :"))
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact * i
    return fact
print("factorial of ",num ,"is :",factorial(num))