def intersect(lst1,lst2):
    res,lst2_copy=[],lst2[:]
    for e1 in lst1:
        if e1 in lst2_copy:
            res.append(e1)
            lst2_copy.remove(e1)
    return res
lst1=[1,2,3,5,7]
lst2=[2,3,4,7]
print(intersect(lst1,lst2))