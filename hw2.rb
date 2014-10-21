# Computes the PV and FV of a leveled cache flow (annunity).
#  c - payment (fixed per period)
#  n - number of periods
#  r - interest rate (per period)
def pv(c, n, r)
  c*(1.0/r)*(1 - (1.0/(1+r)**n))
end
def fv(c, n, r)
 pv(c, n, r) * ((1+r)**n)
end
raise "Error: pv() and fv()" if pv(1000, 10, 0.05) != fv(1000, 10, 0.05)/(1.05)**10

# Computes the payment for a leveled cash flow (annuity).
#  pv - present value (of cash flow)
#  n  - number of periods
#  r  - interest rate (per period)
def pmt(pv, n, r)
  (pv*r)/(1.0 - 1/(1.0+r)**n)
end
raise "Error: pmt()" if pmt(pv(1000, 10, 0.06), 10, 0.06) != 1000.0

#
# Question 8
#
# Two years ago Abilia purchased a $10,000 car; she paid $2000 down and borrowed 
# the rest. She took a fixed rate 60-month instalment loan at a stated rate of 
# 8% per year. Interest rates have fallen during the last two years and she can 
# refinance her car by borrowing the amount she still owes on the car at a new 
# fixed rate of 6% per year for 3 years. Should Abilia refinance her loan? How 
# much will she save per month for the next three years if she decides to 
# refinance?
#
bal = 10000 - 2000
r_8 = 0.08/12
n_8 = 60
p_8 = pmt(bal, n_8, r_8)
n_6 = 3*12
bal = pv(p_8, n_6, r_8)
r_6 = 0.06/12
p_6 = pmt(bal, n_6, r_6)
if (p_6 < p_8)
 "Ans = (Yes, #{(p_8-p_6).round})"
else
 "Ans = (No, #{(p_6-p_8).round})"
end 
