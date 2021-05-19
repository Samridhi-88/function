def harshad(num):
    sum=0
    while(num > 0):
    	rem = num%10
    	sum = sum + rem
    	num = num//10 
    print(sum)   
    if(n %sum == 0):    
        return" harshad number "    
    else:    
        return"not a harshad number "   
n =int(input('enter the number :'))   
harshad(n)
