#Conversion Decimal to Binary...

#var = 24
var = int(input("Enter a Decimal Number : "))
new_var = var
lst = []
while var!=0:
        remain = var%8
        var = var//8
        lst.append(remain)
#print(lst)
rev = lst[-1::-1]
octal = 0
for i in range(len(rev)):
        octal = octal*10+rev[i]
print("Octal Value of {} is {}".format(new_var,octal))

