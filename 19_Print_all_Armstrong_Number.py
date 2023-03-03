#Check Armstrong Number...

n1 = int(input("Enter starting value : "))
n2 = int(input("Enter ending value : "))

while n1<=n2:
        length = len(str(n1))
        sum = 0
        m = n1
        while m!=0:
                a = m%10
                m = m//10
                sum = sum + a**length
        if n1==sum:
                print("Armstrong Number i.e. {}".format(sum))
        #else:
                #print("{} is not Armstrong Number".format(m))
        n1 += 1

