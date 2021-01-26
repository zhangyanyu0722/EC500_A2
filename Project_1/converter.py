# !usr/bin/env python
# ===================================================================================
# Copyright @2021 Yanyu Zhang zhangya@bu.edu
# Project1 : 1 Write python program to convert between C and F.
#            2 Integrate Continuous Build Process to check if your software in each
#              development stage passed the build process.
#            3 Integrate unit test and run the unit test in continuous integration 
#              process.
# ===================================================================================

import numpy as np

# Fahrenheit = (Celsius * 9/5) + 32
def c2f(c):
  if not isinstance(c, float):
    return "ERROR -----> It is not a int"
  
  f = (c * 9 / 5) + 32
  return round(f, 2) # Keep 2 decimals

# Celsius = (Fahrenheit – 32) * 5/9
def f2c(f):
  if not isinstance(f, float):
    return "ERROR -----> It is not a int"
  
  c = (f - 32) * 5 / 9
  return round(c, 2) # Keep 2 decimals
  
