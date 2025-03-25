#first we need to set the env variable using "export <name> = <value>"
import os

n= os.getenv("user") #we need to use os.getenv("<name>") to call it.
print(n)