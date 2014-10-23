# -*- coding: utf-8 -*-
#####################################################################################
#                                  Finance functions                                #
#####################################################################################

# Basic compounding and discounting
# c - amount (single)
# n - number of periods
# r - interest rate (per period)
def compound(c, n, r): return c * ((1+r)**n)
def discount(c, n, r): return c / ((1+r)**n)
comp = compound
disc = discount
assert (comp(1, 1, 1) == 2 and disc(2, 1, 1) == 1), "Test 1.a: Failed"
assert (disc(comp(9, 7, 0.1), 7, 0.1) == 9),        "Test 1.b: Failed"

# Computes the PV and FV of a leveled cache flow (annunity).
# c - payment (fixed per period)
# n - number of periods
# r - interest rate (per period)
def pv(c, n, r): return c*(1.0/r)*(1 - (1.0/(1+r)**n))
def fv(c, n, r): return comp(pv(c, n, r), n, r)
assert (pv(1000, 10, 0.05) == disc(fv(1000, 10, 0.05), 10, 0.05)),                  "Test 2.a: Failed" 
assert (round(pv(100, 1, 0.06), 2) == round(disc(100, 1, 0.06), 2)),                "Test 2.b: Failed" 
assert (round(fv(100, 2, 0.06), 2) == round(comp(100,1,0.06)+comp(100,0,0.06), 2)), "Test 2.c: Failed" 

# Computes the payment for a leveled cash flow (annuity).
# pv - present value (of cash flow)
# n - number of periods
# r - interest rate (per period)
def pmt(pv, n, r): return (pv*r)/(1.0 - 1/(1.0+r)**n)
assert (round(pmt(100, 1, 0.1), 2) == 110),                   "Test 3.a: Failed" 
assert (round(pmt(pv(1000, 10, 0.06), 10, 0.06), 2) == 1000), "Test 3.b: Failed" 

# Composes int() and round()
def rnd(x): return int(round(x))

#####################################################################################
