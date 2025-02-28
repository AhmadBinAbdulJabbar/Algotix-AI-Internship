# using and operator 

def maxOfThree(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3
  
n1 = 2
n2 = 2
n3 = 1  
print(f"The max number between {n1}, {n2} and {n3} is", maxOfThree(n1, n2, n3))
