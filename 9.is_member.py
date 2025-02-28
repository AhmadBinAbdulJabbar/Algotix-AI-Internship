def isMember(x, a):
  l = len(a)
  counter = 0
  while counter < l:
    if x == a[counter]:
      return True
    counter += 1
    
  return False

n = 3
nums = [1,2,3,4]

print(f"The number {n} is in {nums} :", isMember(n, nums))
print(f"The number {5} is in {nums} :", isMember(5, nums))
