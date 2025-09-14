# Mark-13-python
To learn python for devops

## To open a file in python

**with** --> This handles errors and manages external resources.
**open** --> It is a pyhton funtion used to open a file.

To read a file we can use below format

      with open("login_attrmpt.txt","r") as file:
          file_text=file.read()
      print(file_text)
