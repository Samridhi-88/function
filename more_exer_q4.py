def greatest(a,b,c):
	if a>b and a>c:
		return a," a is greatest"
	if b>a and b>c:
		return b," b is greatest"
	if c>a and c>b:
		return c," c is greatest"
	else:
		return "all are equal"
a=int(input("enter number1"))
b=int(input("enter number2"))
c=int(input("enter number3"))
print(greatest(a,b,c))