import re
def zeroes (base, number):
  f = 1
  for i in range(number): f *= i
  m = re.search("0+$", str(f))
  return m.end(0) - m.start(0) + 1