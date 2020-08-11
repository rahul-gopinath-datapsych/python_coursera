'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below
'''


largest_number=None
smallest_number=None

while True:
        try:
            i= input("Enter a number: ")
            i=int(i)
            if largest_number is None:
                largest_number=i
            elif i>largest_number:
                largest_number=i
            if smallest_number is None:
                smallest_number=i
            elif i<smallest_number:
                smallest_number=i
        except:
            if i.upper()=="DONE":
                print("Maximum is",largest_number)
                print("Minimum is",smallest_number)
                quit()
            else:
                print("Invalid input")
                continue



        

