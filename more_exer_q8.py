def new_list(list1,list2):
	c=list1+list2
	i=0
	n_list=[]
	while i<len(c):
		if c[i] not in n_list:
			n_list.append(c[i])
		i+=1
	print(n_list)
list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
new_list(list1,list2)