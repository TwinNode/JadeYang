def sqInRect(a, b):
  if a == b : return None
  res = []
  while b: # while b is not equal to 0
    b, a = sorted([a,b]) # b is shorter
    res += [b]
    a, b = b, a-b # update b as a-b
  return res


def sqInRect(a,b):
    if a== b: return None
    res = []
    while a != b:
        if a > b:
            res.append(b)
            a = a - b
        else:
            res.append(a)
            b = b - a
    res.append(a)
    return res
