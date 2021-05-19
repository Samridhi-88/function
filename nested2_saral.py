# def perfect(n):
#     sum=0
#     i=2
#     while i*i<=n:
#         if n%i==0:
#             sum=sum+i+n/i
#         i+=1
#     if sum==n and n!=1:
#         print("true")
#     else:
#         print("false")
# n=2
# while n<=100:
#     if perfect(n):
#         print(n)
#     n+=1
#     return sum==n
# #n=int(input("enter the "))
# perfect(7)



def perfect_num(n):
    sum=0
    for i in range(1, n):
        if n%i==0:
            sum+=i
    return sum==n
print(perfect_num(7))



def perfect():
   sum = 0
   i=1
   while i<n:
            	if n%i==0:
            		sum += i
            	i+=1
   return sum == n
number = int(input('Enter number: '))
if perfect(number):
    print(number,"is perfect number")
else:
    print(number,"is not perfect number")
  #perfect number