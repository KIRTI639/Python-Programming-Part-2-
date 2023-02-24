a = int(input("Enter coeffient of x^2 :"))
b = int(input("Enter coeffient of x :"))
c = int(input("Enter constant :"))
e= f"{a}x^2+{b}x+{c}=0"
print(e)
d = (b**2 - (4*a*c))
if d ==0:
    print("Real and Equal.")
elif d >0:
    print("Real and Distinct.")
else:
    print("Real and imaginary")        