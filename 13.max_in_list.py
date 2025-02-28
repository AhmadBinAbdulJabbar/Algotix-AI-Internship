def max_in_list(nums:list[int]):
  max = nums[0]
  for i in nums:
    if(i > max):
      max = i
    
  return max

n = [1,2,10,4,5]
print(f"The Max number in List {n}: ", max_in_list(n))