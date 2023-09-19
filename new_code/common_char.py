s1=input("enter first a string: ")
s2=input("enter second a string: ")
a=list(set(s1)& set(s2))
print("common letters are: ")
for i in a:
    print(i)