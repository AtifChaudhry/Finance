#! /usr/bin/ruby

#####################################################################################
#                                  Finance functions                                #
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
def pv(c, n, r, g=0); c*(1.0/(r-g))*(1 - ((1.0+g)**n)/((1.0+r)**n)) end
def fv(c, n, r, g=0); comp(pv(c, n, r, g), n, r); end
raise "Test 2.a: Failed" if pv(1000, 10, 0.05) != disc(fv(1000, 10, 0.05), 10, 0.05)
raise "Test 2.b: Failed" if pv(100, 1, 0.06).round(2) != disc(100, 1, 0.06).round(2)
raise "Test 2.c: Failed" if fv(100, 2, 0.06).round(2) != (comp(100,1,0.06)+comp(100,0,0.06)).round(2)
raise "Test 3.d: Failed" if pv(100, 10, 0.07, 0.05).round != 860

# Computes the payment for a leveled cash flow (annuity).
# pv - present value (of cash flow)
# n - number of periods
# r - interest rate (per period)
def pmt(pv, n, r); (pv*r)/(1.0 - 1/(1.0+r)**n); end
raise "Test 3.a: Failed" if pmt(100, 1, 0.1).round(2) != 110
raise "Test 3.b: Failed" if pmt(pv(1000, 10, 0.06), 10, 0.06).round(2) != 1000

# Net Present Value (NPV) of a cash flow (the initial investment is cf[0])
#  cf - cash flow stream (including any initial investment < 0)
#  r  - the discount rate
# Example:
#  The CF for an intial investment of $100, which pays $0 in the first
#  period, and then pays $150 in the second period will be [-100, 0, 150].
def npv(cf, r)
 pv = 0.0
 cf.each_with_index {|c, n| pv += disc(c, n, r)}
 pv
end
raise "Test 4.a: Failed" if npv([-100, 110], 0.1).round(2) != 0

####
## Example:
##  How to construct leveled and growth cashflows using list comprehensions,
##  and then computing their NPV.
##

n    = 7    # 7 years
r    = 0.10 # 10%/yr
g    = 0.03 # 3%/yr
pmt  = 1000 # $1,000/yr
pv   = 3000 # $3,000
cf_level  = [-pv] + ([pmt] * n)
cf_growth = [-pv] + (0..n-1).map {|i| comp(pmt, i, g).round}
puts "Level  Cashflows = #{cf_level.to_s}"
puts "NPV(Level Cashflows) = $#{npv(cf_level, r).round}"
puts "Growth Cashflows = #{cf_growth.to_s}"
puts "NPV(Growth Cashflows) = $#{npv(cf_growth, r).round}"

#####################################################################################
