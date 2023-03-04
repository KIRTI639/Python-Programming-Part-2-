#Make a Simple Calculator....

while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")
        ch = int(input("\nEnter your Choice : "))
        if ch==1:
                a = eval(input("Enter 1st Number : "))
                b = eval(input("Enter 2nd Number : "))
                print("Addition of {} and {} is {}".format(a,b,a+b))
        elif ch==2:
                a = eval(input("Enter 1st Number : "))
                b = eval(input("Enter 2nd Number : "))
                print("Subtraction of {} and {} is {}".format(a,b,a-b))
        elif ch==3:
                a = eval(input("Enter 1st Number : "))
                b = eval(input("Enter 2nd Number : "))
                print("Multiplication of {} and {} is {}".format(a,b,a*b))
        elif ch==4:
                a = eval(input("Enter 1st Number : "))
                b = eval(input("Enter 2nd Number : "))
                print("Division of {} and {} is {}".format(a,b,a/b))
        elif ch==5:
                a = eval(input("Enter 1st Number : "))
                b = eval(input("Enter 2nd Number : "))
                print("Modulus of {} and {} is {}".format(a,b,a%b))
        elif ch==6:
                print("Thank You")
                break


