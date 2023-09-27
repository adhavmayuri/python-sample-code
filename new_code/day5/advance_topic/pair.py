def find_pairs(l, x):
   pairs = []
   for (i, el_1) in enumerate(l):
      for (j, el_2) in enumerate(l[i+1:]):
        if el_1 + el_2 == x:
         pairs.append((el_1, el_2))
   return pairs
l=[1,2,3,4,5,6]
x=7
output=find_pairs(l,x)

print(output)