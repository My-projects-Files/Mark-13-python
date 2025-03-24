#Arithmetic Operators
a=3
b=4
sum= a+b
diff= a-b
mul=a*b
div=a/b
print("sum of the given numbers are:", sum)
print("difference of the given numbers are:", diff)
print("product of the given numbers are:", mul)
print("quotient of the given numbers are:", div)

#Comparison Operators

equal= a==b
notequal = a!=b
lessandequal= a<=b
grateandequal= a>=b
less= a<b
great= a>b

print("checking if a equal b", equal)
print("checking if a notequal b", notequal)
print("checking if a greater b", great)
print("checking if a less b", less)
print("checking if a lessthen or equal to b", lessandequal)
print("checking if a greaterthen or equal to b", grateandequal)


# Logical Operators

x=True
y=False

r1=x and y
r2=x or y
print("not x:",not x,"not y:",not y)
print("a is not >b:",not (a>b))
print("a is not < b:",not (a<b))
print("x and y:",r1)
print("x or y:",r2)

#Assignment Operators
total =10

total+=2

total-=2

total*=2

total/=2

print("final total post +,-,/,*:", total)

#Identity and Membership Operators

my_list_1=[1,2,3]
my_list_2=[1,2,3]


print(my_list_1 is not my_list_2)
print(3 in my_list_1)
print(1 not in my_list_1)
print(my_list_1 is my_list_2) #its fasle even if it has same contents as it point to diff objects