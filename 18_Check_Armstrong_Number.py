#Check Armstrong Number...

n = int(input("Enter number : "))#370 
length = len(str(n))#3
sum = 0
m = n
while n!=0:
        a = n%10
        n = n//10
        sum = sum + a**length
if m==sum:
        print("Armstrong Number i.e. {}".format(sum))
else:
        print("{} is not Armstrong Number".format(m))
