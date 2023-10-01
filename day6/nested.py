values=[[y*3 for y in range(x)] for x in range(10)]
values=[]
for x in range(10):
    inner=[]
for y in range(x):
         inner.append(y**3)
         values.append(inner)
for inner_list in values:
    print(inner_list)


values = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    values.append(inner)

# Print the output
for inner_list in values:
    print(inner_list)