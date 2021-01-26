# !usr/bin/env python
# ===================================================================================
# Copyright @2021 Yanyu Zhang zhangya@bu.edu
# Project1 : 1 Write python program to convert between C and F.
#            2 Integrate Continuous Build Process to check if your software in each
#              development stage passed the build process.
#            3 Integrate unit test and run the unit test in continuous integration 
#              process.
# ===================================================================================

from converter import *
import pytest

def test_c2f():
	
  assert c2f(0.00) == 32.00
  assert c2f(100.00) == 212.00
  assert c2f(999.00) == 1830.20

  assert c2f("String") == "ERROR -----> It is not a int"
  assert c2f("-123") == "ERROR -----> It is not a int"
  assert c2f("ec500") == "ERROR -----> It is not a int"

  
def test_f2c():
  pass



