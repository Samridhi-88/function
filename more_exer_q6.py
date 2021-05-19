def check(string_list):
	i=0
	list=[]
	while i<len(string_list):
		if string_list[i] not in list:
			list.append(string_list[i])
		else:
			pass
		i+=1
	print(list)
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
check(string_list)
#Q.6 Saral more exercises