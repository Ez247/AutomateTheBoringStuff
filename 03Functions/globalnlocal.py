# Global and local scopes.
# Parameters and variables assigned inside a function are said to exist in the local scope 
# Parameters and variables assigned ouside a function are said to exist in the global scope
""" Important to note and keep in mind that:
    1. A global scope for global variables is created when the program starts and is destroyed when
       the program ends.
    2. A local scope for local variables is created when the function is called and is destroyed when
       the function returns.
"""
""" Why this matters: 
    1. Code in the global scope cannot use any local variables.
    2. Code in the local scope can access global variables.
    3. Code in one function's local scope cannot use variables in another local scope.
    4. You can use the same name for different variables if they are in different scopes
"""

def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0
    
spam()  # prints out 99 coz local scopes can use variables in other local scopes


# Accessing global variables from a local scope
    """ In Python
        Assignment statement = Local variable 
        No assignment statement =  Global variable 
    """
def spam():
    print(eggs)
    
eggs = 42 # global variable 
spam() # prints out 42  