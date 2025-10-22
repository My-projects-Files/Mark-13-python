# Mark-13-python
To learn python for devops

## To open a file in python

**with** --> This handles errors and manages external resources.
**open** --> It is a pyhton funtion used to open a file.

To read a file we can use below format

      with open("login_attrmpt.txt","r") as file:
          file_text=file.read()
      print(file_text)

## What is (if __name__ == "__main__":)

This plays a huge role in the reusability of the code. it ensure that certain code runs only when the file is executed directly, not when it’s imported as a module into another script.

EX: 
      file: math_utils.py

      def add(a, b):
          return a + b
      
      if __name__ == "__main__":
          print(add(2, 3))  # Runs only if you run math_utils.py directly

if we import the file, the print part will not be executed 

      import math_utils
