# Variables

Variables in Python are names that reference values stored in memory. They are brodly divided into two types.

### Global Variables:
It is a variable that is available through the entire program. they are assigned outside of a function definition, when they are called whether inside (or) outside a function, it will return the value.

    name="jack"

### Local Variables:

It is a variable assigned within a function. they cannot be called (or) accessed outside of the body of a function.

    def greet_employee(name):
        greeting="Welcome" + name
        return greeting
