def overlapping(nums1, nums2):
  i = 0
  while i < len(nums1):
    j = 0
    while j < len(nums2):
      if nums1[i] == nums2[j]:
        return True
      j += 1
    
    i += 1
      
  return False

n1 = [1,2,3,4]
n2 = [4,6,7,8]
print(f"The list {n1} and {n2} have a common element -", overlapping(n1, n2))