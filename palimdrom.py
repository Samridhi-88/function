def pal(a):
    s=list(str(a))
    i=1
    w=[]
    while i<=len(s):
        w.append(s[-i])
        i+=1
    if w==s:
        print("palimdrom")
    else:
        print('not palimdrom')
string=input("enter the num")
pal(string)