#For loop
for i in range(9):
    if i==8:
        break
    if i == 5:
        continue
    print ("for loop output:",i)

else:
    print ("loop ends") #it wont get exected if we have a break statement above


#while loop
count=0
while count<8:
    count+=1
    if count==6:
        break
    if count==3:
        continue
    print("while loop output:",count)

else:
    print("loop finish")#it wont get exected if we have a break statement above
    

#input at runtime
a=input("provide the value:") #Takes as string
b=int(input("provide the value:"))
print(a,b)