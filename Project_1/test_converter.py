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
  pass
  
def test_f2c():
  pass

# def test_right(): 
# 	assert alabo2roman(1213) == "MCCXIII"
# 	assert alabo2roman(20) == "XX"
# 	assert alabo2roman(384) == "CCCLXXXIV"
# 	assert alabo2roman(99) == "XCIX"
# 	assert alabo2roman(999) == "CMXCIX"
# 	assert alabo2roman(3000) == "MMM"
# 	assert alabo2roman(100) == "C"
# 	assert alabo2roman(3999) == "MMMCMXCIX"
# 	assert alabo2roman(12) == "XII"
# 	assert alabo2roman(432) == "CDXXXII"

# def test_error():
# 	assert alabo2roman("String") == "ERROR -----> It is not a int"
# 	assert alabo2roman(23.4) == "ERROR -----> It is not a int" 
# 	assert alabo2roman(-3.4) == "ERROR -----> It is not a int"
# 	assert alabo2roman("-123") == "ERROR -----> It is not a int"
# 	assert alabo2roman("osama") == "ERROR -----> It is not a int"
# 	assert alabo2roman(123.5) == "ERROR -----> It is not a int"
# 	assert alabo2roman(-1) == "ERROR -----> It is not in the range [1,3999]"
# 	assert alabo2roman(0) == "ERROR -----> It is not in the range [1,3999]"
# 	assert alabo2roman(4000) == "ERROR -----> It is not in the range [1,3999]"
# 	assert alabo2roman(-400) == "ERROR -----> It is not in the range [1,3999]"
