#to avoid getting unboundlocalerror while modifying the global variable
x=10 #global variable

def fun():
    x=5
    def global_var():
        global x #This is global keyword to call the variable inside the function
        print("global variable pre modification:",x)
        x=15
    def non_local():
        nonlocal x
        x+=2
        print("nonlocal variable calling within the nested function:",x)
    global_var()
    non_local()


fun()

print("Gobal variable post modification:",x)