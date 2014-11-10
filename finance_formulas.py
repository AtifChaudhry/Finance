#! /usr/bin/env python

#####################################################################################
##                                  Finance functions                              ##
#####################################################################################

## Basic compounding and discounting
##  c - amount (single)
##  n - number of periods
##  r - interest rate (per period)
def compound(c, n, r): return c * ((1+r)**n)
def discount(c, n, r): return c / ((1+r)**n)
comp = compound
disc = discount
assert (comp(1, 1, 1) == 2 and disc(2, 1, 1) == 1), "Test 1.a: Failed"
assert (disc(comp(9, 7, 0.1), 7, 0.1) == 9),        "Test 1.b: Failed"

## Computes the PV and FV of a leveled cache flow (annunity).
##  c - payment (fixed per period)
##  n - number of periods
##  r - interest rate (per period)
##  g - (opional) growth rate (per period)
def pv(c, n, r, g=0): return c*(1.0/(r-g))*(1 - ((1.0+g)**n)/((1.0+r)**n))
def fv(c, n, r, g=0): return comp(pv(c, n, r, g), n, r)
assert (pv(1000, 10, 0.05) == disc(fv(1000, 10, 0.05), 10, 0.05)),                  "Test 2.a: Failed" 
assert (round(pv(100, 1, 0.06), 2) == round(disc(100, 1, 0.06), 2)),                "Test 2.b: Failed" 
assert (round(fv(100, 2, 0.06), 2) == round(comp(100,1,0.06)+comp(100,0,0.06), 2)), "Test 2.c: Failed" 

## Computes the payment for a leveled cash flow (annuity).
##  pv - present value (of cash flow)
##  n - number of periods
##  r - interest rate (per period)
def pmt(pv, n, r): return (pv*r*(1.0+r)**n)/((1.0+r)**n - 1)
assert (round(pmt(100, 1, 0.1), 2) == 110),                   "Test 3.a: Failed" 
assert (round(pmt(pv(1000, 10, 0.06), 10, 0.06), 2) == 1000), "Test 3.b: Failed" 

## Net Present Value (NPV) of a cash flow (the initial investment is cf[0])
##  cf - cash flow stream (including any initial investment < 0)
##  r  - the discount rate
## Example:
##  The CF for an intial investment of $100, which pays $0 in the first
##  period, and then pays $150 in the second period will be [-100, 0, 150].
def npv(cf, r):
 pv = 0.0
 for n in range(len(cf)): pv += disc(cf[n], n, r)
 return pv
assert (round(npv([-100, 110], 0.1), 2) == 0), "Test 4.a: Failed"

import numpy as np

## Internal Rate of Return (IRR)
##  cf - cash flow stream (including any initial investment < 0)
irr = np.irr

## Crossover Rate - The rate at which the NPV of the two 
## cash flow streams is equal.
##  cf1 - the first cash flow stream 
##  cf2 - the second cash flow stream
def cxr(cf1, cf2): np.irr(np.array(cf1) - np.array(cf2))

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

## Draw a Cash Flow Diagram for a CF
def cfplot(cf):
    import matplotlib.pyplot as plt
    import matplotlib.lines as mlines
    fig, ax = plt.subplots()
    xmargin = 0.5
    ax.set_xlim(-xmargin, len(cf) - 1 + xmargin)
    ax.set_ylim(min(cf)*(1.1), max(cf)*(1.1))
    # integer ticks
    ax.set_xticks(range(len(cf)))
    # lines
    for i, c in enumerate(cf):
        if c > 0:
            marker = 'k^'
        elif c <0:
            marker = 'kv'
        else:
            marker = 'kd'
        ax.plot(i, c, marker)
        line = mlines.Line2D((i, i), (0, c), 1, lw=2.)
        ax.add_line(line)
    ax.grid()

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


#####################################################################################
