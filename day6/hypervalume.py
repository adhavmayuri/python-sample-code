def hypervalume(*lengths):
    i=iter(lengths)
    v=next(i)
    for length in i:
        v*=length
    return v
print(hypervalume(1,2,3,4,5))