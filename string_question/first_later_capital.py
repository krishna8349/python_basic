from ast import Str


str = "krishna"
# print(str.capitalize())
str = str[0:2].upper() + str[2:len(str)]
print(str)