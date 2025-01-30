### the wrap a function with an additional functionality

def welcome():
    return "Welcome to advance python " 

wel = welcome() ## function copy

#closures -- we have parent function and sub fucntion now the variables inside the parent function can be accesed by sub function
def main_welcome():
    msg = "Hello Everyone"
    def sub_welcome_class():
        print("welcome to advanced python tutorial")
        print(msg)
        print("lets explore advaned python")
        
    return sub_welcome_class()

## function inside a function
def main_welcome(func):
    print("Welcome to python advanced")

 