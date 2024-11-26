#type casting number in string to integer
#Explicit typecasting

string = "15" #it is a string not an integer
number = 10

string_number = int(string) #by using this int()function we convert string into integer,
#but string should be a valid integer to convert into integer

sum = number + string_number

print("The sum of both numbers is ",sum)

#-------------------------------------------
#Implicit typecasting
#python convert onedata type into another by itself

a = 9.9
print(type(a)) #float
b = 8
print(type(b)) #int

c=a+b
print(c)
print(type(c)) #result is float python changed into float itself

