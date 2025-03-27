import os

def exception(f): #this function return two values 
    try:
        files=os.listdir(f)
        return files, None 
    except FileNotFoundError:
        return None, "Folder not present dude, check for spaces before file name and file name"
    except PermissionError:
        return None, "Permission denied "
    


folders=input("provide the folder names with spaces: ")
folder=folders.split(" ")

for f in folder:
    files,error_message=exception(f)
    if files:
        print("====Printing the folers in:"+ f)
        for i in files:
            print (i)
    elif error_message == None:
       print(f"====no files found in {f}")
    else:
       print(f"=====error in {f}:{error_message}")
