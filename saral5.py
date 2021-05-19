#Ab input ka use kar ke user se 2 numbers input lo. Note: Yeh karne ke liye koi function banane ki zaroorat nahi hai. Fir calculator function ko 4 baar call call kar ke inn dono numbers do add, subtract, multiply, divide karo aur result ko 4 alag variables mein daalo. Woh variables ka naam yeh hoga: * add_result add opertion ka result store krega

def add(a,b):
    sum=a+b
    return sum
def subl(c,d):
    subl=c-d
    return subl
def mul(e,f):
    mul=e*f
    return mul
def div(g,h):
    div=g%h
    return div
print(add(20,25))
print(subl(40,3))
print(mul(10,4))
print(div(40,4))
   

 #list_change naam ka ek function ka code likho jo 2 lists jisme integers arguments ki tarah le aur fir unn lists ki woh items jo same index number (kram) pe hain unko multiply kar ke ek nayi list return karvaye. Aapko multiply karne ke liye calculator function ka use karna hai. Normal tareeke se multiply nahi kar sakte ho. Jaise agar hum function ko aise call karenge toh:  


#def calculator(number1,number2):
#    c=[]
#   i=0
#   while i<len(number1):
#       z=number1[i]*number2
#       c.append(z)
#   print(c)
#alculator(number1=[5,10,50,20],number2=[2,20,3,5])




def calculator(number1, number2):
    c=[]
    for i in range(len(number1)):
       z= number1[i]*number2[i]
       c.append(z)
    print(c)
calculator(number1=[5, 10, 50, 20], number2=[2, 20, 3, 5])









