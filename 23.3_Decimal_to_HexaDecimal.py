#Conversion Decimal to HexaDecimal...

#var = 24
var = int(input("Enter a Decimal Number : "))
new_var = var
lst = []
while var!=0:
        remain = var%16
        var = var//16
        if remain==10:
                lst.append('A')
        elif remain==11:
                lst.append('B')
        elif remain==12:
                lst.append('C')
        elif remain==13:
                lst.append('D')
        elif remain==14:
                lst.append('E')
        elif remain==15:
                lst.append('F')
        else:
                lst.append(str(remain))
#print(lst)
rev = lst[-1::-1]
hexa = ''
for i in range(len(rev)):
        hexa = hexa+rev[i]
print("HexaDecimal of {} is {}".format(new_var,hexa))

