def reverse(s : str) -> str:
  rev = ""
  l = len(s) - 1
  while l >= 0:
    rev += s[l]
    l -= 1

  return rev

name = "ahmad bin abdul jabbar"
print(f"Reverse of f{name} is", reverse(name))