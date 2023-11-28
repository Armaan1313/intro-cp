def takeinput():
    a=float(input("Enter First Number: "))
    print("1st number: ",a)
    b=float(input("Enter Second Number: "))
    print("2nd number: ",b)
    c=str(input("Enter Operation: "))
    print("Your operation: ",c)
    return a,b,c

    
def diplayresult():
    a,b,c=takeinput()
    if c=="+":
        result=a+b
        print("final: ",result)    
    
    elif c=="-":
        result=a-b
        print("final: ",result) 
    
    elif c=="*":
        result=a*b
        print("final: ",result) 
    
    elif c=="/":
        result=a/b
        print("final: ",result) 
    else:
        print("invalid operator!")
        
diplayresult()