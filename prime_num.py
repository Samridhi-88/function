def prime_num(n):
    i=1
    counter=0
    while i<=n:
        if n%i==0:
            counter+=1
        i+=1
    if counter==2:
        print("prime number")
    else:
        print("not prime number")
n=int(input("enter the num"))
prime_num(n)
