def calculator(a,b):
	symbol=input("enter symbol ")
	if symbol=="+":
		print(a+b)
	elif symbol=="-":
		print(a-b)
	elif symbol=="*":
		print(a*b)
	elif symbol=="/":
		print(a/b)
	elif symbol=="//":
		print(a//b)
	else:
		print("nothing")
calculator(45,35)