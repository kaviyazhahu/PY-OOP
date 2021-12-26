import functools
def start_end_decorater(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #
        #print("Hi Iam")
        result=func(*args, **kwargs)
        #print("Working in Python")
        return result
    return wrapper

@start_end_decorater
def print_name():
    print("Kaivyazhahu")

#print_name = start_end_decorater(print_name)

#print_name()

@start_end_decorater
def add(x):
    return x + 5

result = add(15)

print(result)