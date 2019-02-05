def armstrongFunc():
    n=int(input("enter a number"))
    m=str(n)
    a=0
    for i in m:
        b=int(i)
        a=a+b**3
    if a==n:
        print("{} is armstrong number".format(n))
    else:
        print("{} is not a armstrong number".format(n))
armstrongFunc()
        
