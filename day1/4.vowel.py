def vowel(ch: str):
  if len(ch) == 1:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'u' or ch == 'o':
      return True
    else:
      return False
  else:
    return False
  
print("a is vowel: ", vowel('a'))
print("2 is vowel: ", vowel('2'))
print("i is vowel: ", vowel('i'))
print("ab is vowel: ", vowel('ab'))