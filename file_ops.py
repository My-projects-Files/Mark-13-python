#To open and read the files and edit an object in it.

def file_ops(path,key,value):
    with open(path,"r") as file:
        lines= file.readlines()
    with open(path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" +value+ "\n")
                print(f"{path} file modified successfuly")
            else:
                file.write(line)

path_f=input("Please provide File Path: ")

key_f=input("please provide the value that need to change: ")

value_f=input("please provide the new value: ")

file_ops(path_f,key_f,value_f)