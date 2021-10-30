def perfect_number():
    i=1
    while i<=100:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j+=1
        if sum==i:
            print(i,"perfect")
        i+=1
perfect_number()

