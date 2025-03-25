import sys #inbuild command line arg

def add(x,y):
    a=x+y
    return(a)

def sub(x,y):
    s=x-y
    return(s)

x= float(sys.argv[1])
ope=sys.argv[2]
y= float(sys.argv[3])

if ope == "add":
    out=add(x,y)
    print(out)
else:
    out=sub(x,y)
    print(out)