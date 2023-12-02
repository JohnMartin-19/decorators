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

#############################################################
#Decorators with arguments
def sweep_floors(time):
    if 1100 < time < 2100:
        print('Sweeping the floors....')
    else:
        print('Im off duty!')

def wash_dishes(time):
    if 100 < time < 2100:
        print('Wasinh dishes....')
    else:
        print('Im off duty!')

def chop(time):
    if 1100 < time < 2100:
        print('chopping')
    else:
        print('Im off duty')


#refactoring the above code

def check_working_hrs(function):
    def wrapper(time):
        if 1100 < time < 2100:
            function(time)
        else:
            print('Im off duty')

    return wrapper


@check_working_hrs
def sweep_floors(time):
    print('Sweeping the floors....')


@check_working_hrs
def wash_dishes(time):
    print('Washing dishes....')

@check_working_hrs
def chop(time):
    print('Chopping....')


sweep_floors(800)
wash_dishes(1300)
chop(1000)