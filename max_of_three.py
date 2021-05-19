# def max_of_two(x,y):
#     if x>y:
#         return x
#     return y
# def max_of_three(x,y,z):
#     return(max_of_two(x,(max_of_two(y,z))))
# print(max_of_three(4,5,6))



def max_num(max_list):

    i=0
    while i<len(max_list):
        j=0
        while j<len(max_list):
            if max_list[i]>max_list[j]:
                print(max_list[j])
            j+=1
        i+=1

max_list = [5,3,2,10]

max_num(max_list)