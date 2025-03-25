#To learn more about variables in pyhon

x=10 #this is a global varaible

def fun():
    y=5 #This is local variable
    print ("inside the function - local y:",y)
    print("inside the function - global x:",x)

fun()

print("outside the funtion-gloabl x:",x)