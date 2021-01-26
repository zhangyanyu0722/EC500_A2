# ======================================
# Example for EC500 A2 Project 1
# Temperature C to/from F
# ======================================

import numpy as np

# Fahrenheit = (Celsius * 9/5) + 32
def c2f(c):
  f = (c * 9 / 5) + 32
  return round(f, 2) # Keep 2 decimals

# Celsius = (Fahrenheit – 32) * 5/9
def f2c(f):
  c = (f - 32) * 5 / 9
  return round(c, 2) # Keep 2 decimals
  
