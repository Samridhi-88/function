def factorial_num(n):
    product=1
    i=n
    while i>0:
        product=product*i
        i=i-1
    return product
n=int(input("enter the num"))
print(factorial_num(n))