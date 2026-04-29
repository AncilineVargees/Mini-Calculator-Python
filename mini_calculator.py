#creating function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
    
#Loop for infinte calculator
while True:

    #Getting Value From User
    a=int(input("Enter First Value : "))
    b=int(input("Enter Second Value : "))
    
    #Choice of function
    print("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("Addition of a and b : ",add(a,b))
    elif choice==2:
        print("Subtraction of a and b : ",sub(a,b))
    elif choice==3:
        print("Multiplication of a and b : ",mul(a,b))
    elif choice==4:
        if b==0:
            print("Can't divide by 0")
        else:
            print("Division of a and b : ",div(a,b)) 
    else:
        print("Invalid")

    #loop
    again=input("Do you want to continue : Yes/No")
    if again.lower() !="yes":
        break
