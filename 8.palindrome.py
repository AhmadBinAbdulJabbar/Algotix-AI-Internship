# first approach using the reverse function
# def reverse(s : str) -> str:
#   rev = ""
#   l = len(s) - 1
#   while l >= 0:
#     rev += s[l]
#     l -= 1

#   return rev

# def is_palindrome(s : str):
#   string_reverse = reverse(s)
#   if string_reverse == s:
#     return True
#   else:
#     return False
  

# 2nd approach better approach
def is_palindrome(s : str):
  l = 0
  r = len(s) - 1
  while(l < r):
    if s[l] != s[r]:
      return False
    
    l += 1
    r -= 1

  return True


s = "radar"
print(f"The string {s} is palindrome: ", is_palindrome(s))
print(f"The string {s} is palindrome: ", is_palindrome("banana"))

