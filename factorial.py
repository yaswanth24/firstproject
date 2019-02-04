def factorialFunc():
    n=int(input("enter a number"))
    a=1
    for i in range(1,n+1):
        a=a*i
    print("factorial of {} is {}".format(n,a))
factorialFunc()
    
