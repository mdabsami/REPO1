def checking(arg1):
    if arg1 %2==0:
        print("The number is even")
    else:
        print("The number is odd")
        
        
def main():
    num1=int(input("Enter a number: "))
    
    if num1.isdigit():
        checking(num1)
    else:
        print("Entered an invalid option. Qutting the program....")
        
        
 if _name_=="_main_":
     main()