#Area if Triangle
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is = {}".format(area))
