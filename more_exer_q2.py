def expenses_numberOfStudents(a,b):
	if a*b<=50000:
		return "hum budget ke ander hai"
	if a*b>50000:
		return "hum budget ke bahar hai"
	else:
		pass
a=int(input("enter number of students"))
b=int(input("enter expenses"))
print(expenses_numberOfStudents(a,b))
#saral Q.2 more exercises
