transposed=[]
matrix=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
for i in range(4):
    transposed.append([row[i] for row in matrix ])
print(transposed)