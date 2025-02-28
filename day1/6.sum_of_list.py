def sum(nums: list[int]):
  sum = 0
  for n in nums:
    sum += n
  
  return sum

numbers = [1, 2, 3, 4]
print("Sum of all numbers in list [1, 2, 3, 4]", sum(numbers))

# print("Sum of list [1, 2, 3, 4]", sum(2))
# this will give error