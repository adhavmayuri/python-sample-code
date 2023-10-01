def convert_upper(f):
    print("convert upper")
    def wrap(*args, **kwargs):
        print("wrap")
        x = f(*args, **kwargs)
        return x.upper()
    return wrap

@convert_upper
def my_name(name):
    print("my_name")
    return name

result = my_name("John")

print("Result:", result)










