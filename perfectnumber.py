def perfectFunc():
    n=int(input("enter a number"))
    m=0
    for i in range(1,n):
        if n%i==0:
            m=m+i
    if m==n:
        print("{} is perfect number".format(n))
    else:
        print("{} is not a perfect number".format(n))
perfectFunc()
#ufdjnougohldgnoiviflkjvrihvnoirhgvnbrvijkfjnoi
