# Find HCF (Highest Common Factor) or GCD (Greatest Common Divisor)

n1 = int(input("Enter first Number : "))
n2 = int(input("Enter second Number : "))
if n1>n2:
        smaller = n2
else:
        smaller = n1

for i in range(1,smaller+1):
        if n1%i==0 and n2%i==0:
                HCF = i
print("The H.C.F. of {} and {} is {}.".format(n1,n2,HCF))
