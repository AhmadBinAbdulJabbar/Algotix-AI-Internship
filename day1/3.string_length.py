def stringLength(str):
  count = 0
  for char in str:
    count += 1
  
  return count

name =  "ahmad bin abdul jabbar"
print(f"The length of the string {name}", stringLength(name))
# for checking if my function is giving correct value
print(f"The length of the string {name}", len(name))
