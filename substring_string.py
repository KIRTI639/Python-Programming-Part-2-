# 6. Write a Python program to get a char in a string just before specified substring.
string = input("Enter the string ::::: ")
sub_string = input("Enter the substring :::::") 
index = string.index(sub_string)
# print(index)
a = string[index-1]
print(a)
