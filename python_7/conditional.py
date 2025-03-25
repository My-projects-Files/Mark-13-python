#Conditional statement 

import sys

type= sys.argv[1]

if type == "t2.micro":
    print("it will be charged 2 dollers pre day")
elif type == "t2.medium":
    print("it will be charged 4 dollers per day")
elif type == "t2.xlarge":
    print("it will be charged 8 dollers per day")
else:
    print("please provide a valid instace type")