def findmediansortedarray(nums1,nums2):
  merg=nums1.copy()
  merg.extend(nums2)
  merg.sort()
  if len(merg)%2!=0:
    return float(merg[len(merg)]//2)
  else:
    a=merg[len(merg)//2-1]
    b=merg[len(merg)//2]
    return float(a+b)/2
nums1=[1,3]
nums2=[2,4]
result=findmediansortedarray(nums1,nums2)
print(result)