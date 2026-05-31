CHANGE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def dec_2_fact_string(dec: int) -> str:
  i = 1
  res = []

  while dec > 0 or i == 1:
    remainder = dec % i
    remainder = CHANGE[remainder] # if remainder >= 0, becomes an alphabet letter
    dec //= i
    i += 1
    res.append(remainder)
  return "".join(map(str, res[::-1]))

def fact_string_2_dec(fact: str) -> int:
  new_fact = fact[::-1]
  i = total = 0
  multipler = 1

  while i < len(new_fact) :
    num = CHANGE.index(new_fact[i]) # if new_fact[i] is alphabet, get its index number
    total += num * multiplier
    i += 1
    multiplier *= i
  return total

dec = 463 
# output needs to be "341010" for the first function
