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
def bas_asc():
  a = input("#s you want to add, seperate with spaces: ")
  a = a.split(" ")
  b = input("#s you want to subtract, seperate with spaces: ")
  b = b.split(" ")
  c = 0
  for d in a:
    c += int(d)
  for e in b:
    c -= int(e)
  return c
def bas_mdc():
  a = input("#s you want to multiply, seperate with spaces: ")
  a = a.split(" ")
  b = input("#s you want to divide by, seperate with spaces: ")
  b = b.split(" ")
  c = 1
  for d in a:
    c *= int(d)
  for e in b:
    c /= int(e)
  return c
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
def qua_vef():
  h, k = qua_ver()
  a = float(input("a again: "))
  if h < 0:
    if k < 0:
      return f"{a}(x{h})^2{k}"
    else:
      return f"{a}(x{h})^2+{k}"
  elif k < 0:
    return f"{a}(x-{h})^2{k}"
  else:
    return f"{a}(x-{h})^2+{k}"
def qua_vts():
  h = float(input("x coordinate of vertex: "))
  k = float(input("y coordinate of vertex: "))
  a = float(input("a: "))
  
def rit_pll():
  a = float(input("Leg: "))
  b = float(input("Leg: "))
  c = (a ** 2) + (b ** 2)
  return c ** .5
def rit_phl():
  a = float(input("Hypotenuse: "))
  b = float(input("Leg: "))
  c = (a ** 2) - (b ** 2)
  return c ** .5
def rit_che():
  a = float(input("Leg: "))
  b = float(input("Leg: "))
  c = float(input("Hypotenuse: "))
  return (a ** 2) + (b ** 2) == c ** 2
def rit_gen():
  a = int(input("Odd number: "))
  b = (a ** 2) / 2
  c = b - .5
  d = b + .5
  return c, d
def rit_sin():
  a = float(input("Opposite: "))
  b = float(input("Hypotenuse: "))
  return a / b
def rit_cos():
  a = float(input("Adjacent: "))
  b = float(input("Hypotenuse: "))
  return a / b
def rit_tan():
  a = float(input("Opposite: "))
  b = float(input("Adjacent: "))
  return a / b
def cir_two_per():
  r = float(input("Radius: "))
  pi = 3.14
  return 2 * pi * r
def cir_two_are():
  r = float(input("Radius: "))
  pi = 3.14
  return pi * r * r
def cir_sph_sar():
  r = float(input("Radius: "))
  pi = 3.14
  return 4 * pi * r * r
def cir_sph_vol():
  r = float(input("Radius: "))
  pi = 3.14
  return 4 / 3 * pi * r * r * r
def cir_cyl_sar():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  pi = 3.14
  return 2 * pi * r * ( r + h )
def cir_cyl_vol():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  pi = 3.14
  return pi * r * r * h
def cir_con_sar():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  a = h ** 2 + r ** 2
  pi = 3.14
  return pi * r * ( r + a ** .5 )
def cir_con_vol():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  pi = 3.14
  return pi * r * r * h / 3
def cir_con_las():
  r = float(input("Radius: "))
  h = float(input("Height: "))
  a = h ** 2 + r ** 2
  pi = 3.14
  return pi * r * ( a ** .5 )
def cal_bas():
  p = input("Bas Operation: ")
  if p == "add":
    return bas_add()
  elif p == "sub":
    return bas_sub()
  elif p == "mul":
    return bas_mul()
  elif p == "div":
    return bas_div()
  elif p == "rem":
    return bas_rem()
  elif p == "asc":
    return bas_asc()
  elif p == "mdc":
    return bas_mdc()
  else:
    return "You didn\'t pick a bas operation. Try add, sub, mul, div, or rem."
def cal_mul():
  p = input("Mul Operation: ")
  if p == "exp":
    return mul_exp()
  elif p == "roo":
    return mul_roo()
  elif p == "fac":
    return mul_fac()
  else:
    return "You didn\'t pick a mul operation. Try exp, roo, or fac."
def cal_qua():
  p = input("Qua Operation: ")
  if p == "roo":
    return qua_roo()
  elif p == "sol":
    return qua_sol()
  elif p == "ver":
    return qua_ver()
  elif p == "fac":
    return qua_fac()
  elif p == "vef":
    return qua_vef()
  else:
    return "You didn\'t pick a qua operation. Try roo, sol, ver, or fac."
def cal_rit():
  p = input("Rit Operation: ")
  if p == "pll":
    return rit_pll()
  elif p == "phl":
    return rit_phl()
  elif p == "gen":
    return rit_gen()
  elif p == "che":
    return rit_che()
  elif p == "sin":
    return rit_sin()
  elif p == "cos":
    return rit_cos()
  elif p == "tan":
    return rit_tan()
  else:
    return "You didn\'t pick a rit operation. Try pll, phl, gen, che, sin, cos, or tan."
def cal_cir():
  p = input("Cir Shape: ")
  if p == "two":
    q = input("Two Formula: ")
    if q == "per":
      return cir_two_per()
    elif q == "are":
      return cir_two_are()
    else:
      return "You didn't pick one of our formulas. Try per or are"
  elif p == "sph":
    q = input("Sph Formula: ")
    if q == "sar":
      return cir_sph_sar()
    elif q == "vol":
      return cir_sph_vol()
    else:
      return "You didn't pick one of our formulas. Try sar or vol"
  elif p == "cyl":
    q = input("Cyl Formula: ")
    if q == "sar":
      return cir_cyl_sar()
    elif q == "vol":
      return cir_cyl_vol()
    else:
      return "You didn't pick one of our formulas. Try sar or vol"
  elif p == "con":
    q = input("Con Formula: ")
    if q == "sar":
      return cir_con_sar()
    elif q == "vol":
      return cir_con_vol
    elif q == "las":
      return cir_con_las
    else: 
      return "You didn't pick one of our formulas. Try sar, vol, or las"
  else:
    return "You didn't pick one of our shapes. Try two, sph, cyl, or con"
def cal_mai():
  o = input("Section: ")
  if o == "bas":
    return cal_bas()
  elif o == "mul":
    return cal_mul()
  elif o == "qua":
    return cal_qua()
  elif o == "rit":
    return cal_rit()
  elif o == "cir":
    return cal_cir()
  else:
    return "You didn\'t pick one of the sections we have operations for. Try bas, mul, qua, rit, or cir"
print(cal_mai())