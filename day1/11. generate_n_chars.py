def  generate_n_chars(n : int, ch) -> str:
  count = 0
  result = ""
  while count < n:
    result += ch
    count += 1
  
  return result

print("x 5 time by passing (5, x):", generate_n_chars(5, "x"))