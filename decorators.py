def decorator(function):
    def wrapper():
        print("Before calling the function(about to be called)")
        #function()
        print("After calling the function(already called)")
        function()
    return wrapper

@decorator
def get_called():
    print("Function thats being called")


#now instanciating an obj
lets_call = decorator(get_called)
lets_call()