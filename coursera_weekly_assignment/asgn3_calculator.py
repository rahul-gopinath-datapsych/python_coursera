'''
Requirement: 
Calculator for Add, Sub, Div and multiple
Additional Test Features Added and utilized few concepts of python.
1. Gave user 3 try's for every execute.
2. Added slicing concept to determine operations even if there is any adhoc input or typo
    Eg: Add, Adding, Addition, A, Asd, Adsitp etc.. (Any error will be ignored and still compute addition)
3. Added Cache mechanism to let user know the mistake they are doing instead of raw error. So, that it
can be user friendly. Below are the errors that would be caputred and let user know to correct it.
    1. Entering String instead of a integer. (It will tell which input value the user entered string instead of int)
    2. Leaving any of the input blank. (It will tell which input value the user left blank)
    3. Using different operations rather that add, subtract, division and multiplication.
    4. 
'''

#Calculator function
def calculator(a,b,op):
    try:
        a=int(a)
        b=int(b)
        if op[0].upper()=="A":
            result=a+b
        elif op[0].upper()=="D":
            result=a/b
        elif op[0].upper()=="M":
            result=a*b
        elif op[0].upper()=="S":
            result=a-b
        return print("Output:",result)
    except:
        if len(op)==0:
            print("Oops! You left the operation empty")
        elif (op[0].upper()!="A" and op[0].upper()!="D" and op[0].upper()!="M" and op[0].upper()!="S"):
            print("Oops! You entered a wrong operation")
        if len(str(a))==0:
            print("Oops! You left 1st number blank. Sorry, I'm Unable to decide")
        elif isinstance(a,int) is False:
            print("Oops! You entered string instead of a number for 1st input ")
        if len(str(b))==0:
            print("Oops! You left 2nd number blank. Sorry, I'm Unable to decide")
        elif isinstance(b,int) is False:
            print("Oops! You entered string instead of a number for 2nd input ")


#Invoking the function for 3 try's from a user
i=0
while i<3:
    #Taking input parameter from the user
    a=input("Enter the 1st number: ")
    b=input("Enter the 2nd number: ")
    op=input("Enter Basic operation to compute: ")
    calculator(a,b,op)
    i=i+1





