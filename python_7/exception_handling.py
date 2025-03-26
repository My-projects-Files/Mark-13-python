#try for exception prone code
a1=float(input("provide a number :"))
a2=float(input("Provide a number :"))

try:
    x=a1/a2      #code where error might occur
except ZeroDivisionError:
    print("cant divide with 0 dude")  #prints when ZeroDivisionError occurs
else:
    print("This is the result:",x) #Prints if no error occurs
finally:
    print("im inevitable")  #prints even if error occurs or not 
