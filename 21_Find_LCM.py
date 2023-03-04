#Program to find LCM (Least Common Multiple)

n1 = int(input("Enter first Number : "))
n2 = int(input("Enter second Number : "))
if n1<n2:
        greater = n2
else:
        greater = n1
while True:
        if greater%n1==0 and greater%n2==0:
                print("The L.C.M. of {} and {} is {}.".format(n1,n2,greater))
                break
        greater+=1
