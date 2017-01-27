# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:23 2017

@author: beatobongco
"""

import math

def polysum(n, s):
  """Return a polysum of a polygon, rounded to 4 decimal places.

  Polysum is defined as area of polygon + perimeter squared.

  n -- number of sides of the polygon
  s -- length of each side of the polygon
  """
  area = (0.25*n*s**2) / math.tan(math.pi/n)
  perimeter = n * s

  return round(area + perimeter**2, 4)

## Some tests to make sure everything works
assert polysum(33, 89) == 9310326.8357
assert polysum(85, 72) == 40433569.1586
