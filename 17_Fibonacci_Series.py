# Generate Fibonacci Series...

n = int(input("Enter Number of Terms : "))
f0 = -1
f1 = 1
for i in range(n):
        f2 = f0+f1
        print(f2, end="  ")
        f0 = f1
        f1 = f2
        
