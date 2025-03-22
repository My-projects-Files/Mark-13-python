#To learn more about variables in pyhon

x=10 #this is a global varaible

def fun():
    y=5 #This is local variable
    print ("inside the function - local y:",y)
    print("inside the function - global x:",x)

fun()

print("outside the funtion-gloabl x:",x)

#to avoid getting unboundlocalerror while modifying the global variable

def fun_1():
    global x #This is global keyword to call the variable inside the function
    print("global variable pre modification:",x)
    x=15

fun_1()

print("Gobal variable post modification:",x)