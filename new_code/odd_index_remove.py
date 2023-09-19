def modify(string):
    final=" "
    for i in range (len(string)):
        if i%2==0:
            final=final+string[i]
    return final
string=input("enter a string: ")
print("modify string is ")
print(modify(string))