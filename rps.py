a=int(input("enter a value"))
b=int(input("enter a value"))
c=int(input("enter a value"))
#1 =rock,2=paper,3=scissors
if(a==1): 
    if(b==2):
        print("b won")
    else: 
        print("a won")
elif(a==2): 
    if(b==1):
        print("a won")
    else: 
        print("b won") 
elif(a==3): 
    if(b==1): 
        print("b won")
    else: 
       print("a won")
else:
    print("both r winners")