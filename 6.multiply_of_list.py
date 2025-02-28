def multiply(nums: list[int]):
  mul = 1
  for n in nums:
    mul *= n

  return mul

numbers = [1, 2, 3, 4]
print("Multiply of all list numbers is: ", multiply(numbers))

# if list is not passed it will give error
# print("Multiply of all list numbers is: ", multiply(2))