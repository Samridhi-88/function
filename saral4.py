def check_number(a=4,b=5):
    if a%2==0 and b%2==0:
        print("dono even")
    else:
        print("dono even nhi hai")
check_number()


def check_number_list(n,m):	
	i=0
	while i<len(n):
		if n[i]%2==0 and m[i]%2==0:
			print("even")
		else:
			print("not even")
		i=i+1
n=[2,6,18,10,3,75]
m=[6,19,24,12,3,87]
check_number_list(n,m)