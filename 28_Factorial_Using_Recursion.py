#Factorial Using Recursion.....

def fact(n):
        f = 1
        if n==1:
                return 1
        else:
                f = f*n*fact(n-1)
                return f

f1 = fact(3)
print(f1)
