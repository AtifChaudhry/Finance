#! /usr/bin/env python

###############################################################################
##                                  Finance functions                        ##
###############################################################################

## Basic compounding and discounting
##  c - amount (single)
##  n - number of periods
##  r - interest rate (per period)
def compound(c, n, r): return float(c) * ((1+r)**n)
def discount(c, n, r): return float(c) / ((1+r)**n)
comp = compound
disc = discount
assert (comp(1, 1, 1) == 2 and disc(2, 1, 1) == 1), "Test 1.a: Failed"
assert (disc(comp(9, 7, 0.1), 7, 0.1) == 9),        "Test 1.b: Failed"

## Computes the PV and FV of a leveled cache flow (annunity).
##  c  - payment (fixed per period)
##  n  - number of periods
##  r  - interest rate (per period)
##  g  - (opional) growth rate (per period)
##  fv - (optional) future value of an additional final cashflow
def pv(c, n, r, g=0, fv=0): 
 return c*(1.0/(r-g))*(1 - ((1.0+g)**n)/((1.0+r)**n)) + disc(fv,n,r)
def fv(c, n, r, g=0): 
 return comp(pv(c, n, r, g), n, r)
assert (pv(1000, 10, 0.05) == disc(fv(1000, 10, 0.05), 10, 0.05)),                  "Test 2.a: Failed" 
assert (round(pv(100, 1, 0.06), 2) == round(disc(100, 1, 0.06), 2)),                "Test 2.b: Failed" 
assert (round(fv(100, 2, 0.06), 2) == round(comp(100,1,0.06)+comp(100,0,0.06), 2)), "Test 2.c: Failed" 

## Computes the payment for a leveled cash flow (annuity).
##  pv - present value (of cash flow)
##  n  - number of periods
##  r  - interest rate (per period)
##  fv - (optional) future value of an additional final cashflow
def pmt(pv, n, r, fv=0): return ((pv - disc(fv,n,r))*r*(1.0+r)**n)/((1.0+r)**n - 1)
assert (round(pmt(100, 1, 0.1), 2) == 110),                   "Test 3.a: Failed" 
assert (round(pmt(pv(1000, 10, 0.06), 10, 0.06), 2) == 1000), "Test 3.b: Failed" 
assert (round(pmt(916.56,14,0.08, fv=1000)) == float(70)),    "Test 3,c: Failed"

## Net Present Value (NPV) of a cash flow (the initial investment is cf[0])
##  cf - cash flow stream (including any initial investment at time=0)
##  r  - the discount rate
## Example:
##  The CF for an intial investment of $100, which pays $0 in the first
##  period, and then pays $150 in the second period will be [-100, 0, 150].
def npv(cf, r):
 return reduce((lambda pv,(n,c): pv+disc(c,n,r)), enumerate(cf), 0.0)

assert (round(npv([-100, 110], 0.1), 2) == 0), "Test 4.a: Failed"


## Internal Rate of Return (IRR)
##  cf - cash flow stream (including any initial investment < 0)
import numpy as np
irr = np.irr

## Composes int() and round()
def rnd(x): return int(round(x))

## Store/Print an array of string as numbered lines.
import locale
class Answers(object):
 def __init__(self):
  self.ans = []
  locale.setlocale(locale.LC_ALL, '')
 def add(self, x, currency = False):
  self.ans.append(x)
  return locale.currency(x, grouping=True)[:-3] if currency else x
 def amt(self, x):
  return self.add(x, True)
 def display(self):
  for i, v in enumerate(self.ans): 
   print("%2d. %s" % (i+1, str(v)))

####
## Example:
##  How to construct leveled and growth cashflows using list comprehensions,
##  and then computing their NPV.
##
if __name__ == "__main__":
 import finance_formulas as fi

 n    = 7    # 7 years
 r    = 0.10 # 10%/yr
 g    = 0.03 # 3%/yr
 pmt  = 1000 # $1,000/yr
 pv   = 3000 # $3,000
 cf_level  = [-pv] + ([pmt] * n)
 cf_growth = [-pv] + [fi.rnd(fi.comp(pmt, i, g)) for i in range(n)]
 print "Level  Cashflows =", cf_level
 print "NPV(Level Cashflows) = $%d" % fi.npv(cf_level, r)
 print "Growth Cashflows =", cf_growth
 print "NPV(Growth Cashflows) = $%d" % fi.npv(cf_growth, r)


################################################################################
