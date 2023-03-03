#Sum of Natural Number...

n = int(input("Enter Number of Terms : "))
sum = 0
for i in range(1,n+1):
        print(i, end = "  ")
        sum+=i
print("\nSum of Natural Number is {}".format(sum))
