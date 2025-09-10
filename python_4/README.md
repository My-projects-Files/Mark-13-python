# Functions and Modules:

## Functions :
It is a section of code that can be reused in a program. they allow us to automate repetitive parts of our code.

Functions are of two types.

1) **Built in functions** --> They are functions that exist within python and can be called directly.
   
       print()

2) **User defined function** --> They are functions that programmers design for their specific needs. to define a function, we need to include a function header and the body of a function.

       def display_message():
           print("to investigate activity")
       display_message()

## Parameters:
it is an object that is included in a function definition for use in that function. when we define a function, we create variables in the function header. they can be used in function body.


    def display_message(user):
        Print("To investigate activity of " , user)
    display_message(Tony)

## Module:
It is a python file that contains additional functions, variables, classes, and any kind of runnable code.



### Importing an entire module:

To import an entire python standard library module, we can use the "import" keyword. it searches for a module (or) library in a system and adds it to the local python env.

    import statistics
    failed_attempts=[20,17,15,21]
          median_failed=statistics.median(failed_attempts)
    print(median_failed)

### Specific function from module:

We can import specific funtion from the python standard Library, but if we import specific function, we no longer have to specify the name of the module before the function.

      from statistics import mean, median
      failed=[20,17,178,21,19]
      mean_failed = mean(failed)
      median_failed = median(failed)
      print(mean_failed,median_failed)

## Library:
It is a collection of modules that provide code users can access in their programs.

**Python standard Library** : It is an extensive collection of usable pyhton code that often comes packaged with python.

### External Libraries:

In additional to python standard Library, we can also download external libraries and incorporate into our python code.

- first we need to install them

      pip install numpy
  
- now we can import those librarys

      import numpy
