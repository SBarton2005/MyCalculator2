def bas_add():
  a = input("#s you want to add, seperate with spaces: ")
  a = a.split(" ")
  c = 0
  for b in a:
    c += float(b)
  return c
def bas_sub():
  a = input("# you want to subtract from: ")
  b = input("# you want to subtract: ")
  return float(a) - float(b)
def bas_mul():
  a = input("#s you want to multiply, seperatre with spaces: ")
  a = a.split(" ")
  c = 1
  for b in a:
    c *= float(b)
  return c
def bas_div():
  print("This is to divide a number, if you want to get the remainder try \'bas_rem\'")
  a = input("# you want to be divided: ")
  b = input("# you want it to be divided by: ")
  return float(a) / float(b)
def bas_rem():
  print("This is to get the remainder, if you want to divide a number try \'bas_div\'")
  a = input("# you want to be divided: ")
  b = input("# you want it to be divided by: ")
  return float(a) % float(b)
def mul_exp():
  a = input("Base: ")
  b = input("Exponent: ")
  return float(a) ** int(b)
def mul_roo():
  a = input("Radicand: ")
  b = input("Index: ")
  return float(a) ** (1 / int(b))
def mul_fac():
  a = int(input("Factorial of: "))
  i = 1
  if a > 0:
    while a > 0:
      i *= a
      a -= 1
    return i
  else:
    return "You can only find the factorial of a natural number"
def qua_roo():
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))
  d = (b ** 2) - (4 * a * c)
  e = d ** .5
  fa = - b + e
  fb = - b - e
  ga = fa / 2 / a
  gb = fb / 2 / a
  return ga, gb
def qua_ver():
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))
  x = - b / 2 / a
  y = (a * x* x) + (b * x) + c
  return x, y
def qua_sol():
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))
  x = float(input("x: "))
  y = (a * x * x) + (b * x) + c
  return y
def qua_fac():
  xa, xb = qua_roo()
  if xa < 0:
    if xb < 0:
      return f"(x+{xa*-1})(x+{xb*-1})"
    return f"(x+{xa*-1})(x-{xb})"
  if xb < 0:
    return f"(x-{xa})(x+{xb*-1})"
  return f"(x-{xa})(x-{xb})"
