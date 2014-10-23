#####################################################################################
# Finance functions #
#####################################################################################
# Basic compounding and discounting
# c - amount (single)
# n - number of periods
# r - interest rate (per period)
def compound(c, n, r); c * ((1+r)**n); end
def discount(c, n, r); c / ((1+r)**n); end
def comp(c,n,r); compound(c,n,r); end
def disc(c,n,r); discount(c,n,r); end
raise "Test 1.a: Failed" if comp(1, 1, 1)!=2 or disc(2, 1, 1)!=1
raise "Test 1.b: Failed" if disc(comp(9, 7, 0.1), 7, 0.1) != 9
# Computes the PV and FV of a leveled cache flow (annunity).
# c - payment (fixed per period)
# n - number of periods
# r - interest rate (per period)
def pv(c, n, r); c*(1.0/r)*(1 - (1.0/(1+r)**n)); end
def fv(c, n, r); comp(pv(c, n, r), n, r); end
raise "Test 2.a: Failed" if pv(1000, 10, 0.05) != disc(fv(1000, 10, 0.05), 10, 0.05)
raise "Test 2.b: Failed" if pv(100, 1, 0.06).round(2) != disc(100, 1, 0.06).round(2)
raise "Test 2.c: Failed" if fv(100, 2, 0.06).round(2) != (comp(100,1,0.06)+comp(100,0,0.06)).round(2)
# Computes the payment for a leveled cash flow (annuity).
# pv - present value (of cash flow)
# n - number of periods
# r - interest rate (per period)
def pmt(pv, n, r); (pv*r)/(1.0 - 1/(1.0+r)**n); end
raise "Test 3.a: Failed" if pmt(100, 1, 0.1).round(2) != 110
raise "Test 3.b: Failed" if pmt(pv(1000, 10, 0.06), 10, 0.06).round(2) != 1000
#####################################################################################
