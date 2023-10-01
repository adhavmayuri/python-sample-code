t=(1,2,3,4,5)
def print_args(arg1,arg2,*args):
    print(arg1)
    print(arg2)
    print(*args)
print_args(*t)