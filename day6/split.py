def split(n):
    tens=n/10
    ones=n%10
    return(tens,ones)
x=83
ten,one=split(x)
print("%d has tens digit %d and ones digit %d" %(x,ten,one))