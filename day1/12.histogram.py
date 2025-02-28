def printStars(n : int):
  s = ""
  for i in range(0, n):
    s += "*"

  return s
  

def histogram(nums : list[int]):
  for n in nums:
    print(printStars(n))


histogram([4, 9, 7])
