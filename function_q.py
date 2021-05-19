def student(budget):
	i= 1
	while i<=100:
		if budget<=50000:
			print('budget ke under hai')
			break
		elif budget>50000:
			print('hum budget ke bahar hai')
			break
		else:
			pass
		i= i+1
student(budget= int(input('enter no. ')))
			# saral ka khrcha se thora aalg