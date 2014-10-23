# -*- coding: utf-8 -*-
#####################################################################################
#                                  Finance functions                                #
#####################################################################################

# Basic compounding and discounting
#  c - amount (single)
#  n - number of periods
#  r - interest rate (per period)
def compound(c, n, r); c * ((1+r)**n); end
def discount(c, n, r); c / ((1+r)**n); end
def comp(c,n,r); compound(c,n,r); end
def disc(c,n,r); discount(c,n,r); end
raise "Test 1.a: Failed" if comp(1, 1, 1)!=2 or disc(2, 1, 1)!=1 
raise "Test 1.b: Failed" if disc(comp(9, 7, 0.1), 7, 0.1) != 9

# Computes the PV and FV of a leveled cache flow (annunity).
#  c - payment (fixed per period)
#  n - number of periods
#  r - interest rate (per period)
def pv(c, n, r); c*(1.0/r)*(1 - (1.0/(1+r)**n)); end
def fv(c, n, r); comp(pv(c, n, r), n, r); end
raise "Test 2.a: Failed" if pv(1000, 10, 0.05) != fv(1000, 10, 0.05)/(1.05)**10
raise "Test 2.b: Failed" if pv(100, 1, 0.06).round(2) != disc(100, 1, 0.06).round(2)
raise "Test 2.c: Failed" if fv(100, 2, 0.06).round(2) != (comp(100,1,0.06)+comp(100,0,0.06)).round(2)

# Computes the payment for a leveled cash flow (annuity).
#  pv - present value (of cash flow)
#  n  - number of periods
#  r  - interest rate (per period)
def pmt(pv, n, r); (pv*r)/(1.0 - 1/(1.0+r)**n); end
raise "Test 3.a: Failed" if pmt(100, 1, 0.1).round(2) != 110
raise "Test 3.b: Failed" if pmt(pv(1000, 10, 0.06), 10, 0.06) != 1000

#####################################################################################

# Collect answers in the ans array
ans = []

# Question 1
# (5 points) Carlos goes to the bank to take out a personal loan. The stated annual 
# interest rate is 12%, but interest is compounded monthly and he will make monthly 
# payments. The effective annual interest rate (EAR) of the loan is less than 12%. 
ans << false

# Question 2
# (5 points) Gloria is 35 and trying to plan for retirement. She has put a budget
# together and plans to save $4,800 per year, starting at the end of this year, 
# in a retirement fund until she is 65. Assume that she can make 7% on her account. 
# How much will she have for retirement at age 65? 
n = 65 - 35
r = 0.07
c = 4800
ans <<  fv(c, n, r).round

# Question 3
# (5 points) Mohammad has just turned 21 and now has access to the money his parents 
# have been putting away in an account for him since he was 5 years old. His mother 
# has asked him to guess what his account is worth given that they have invested 
# $1,000 every year in the account starting on his 5th birthday and have just made one. 
# The interest rate on the account has been 3.5% annually. 
# How much is Mohammad’s account worth today? 
n = 21 - 5 + 1
r = 0.035
c = 1000
ans << fv(c, n, r).round

# Question 4
# (5 points) Marcel has just graduated from college and has found a job that will pay 
# him $25,000 per year at the end of each year, but the job is only for 5 years. 
# He is not worried about that because he plans to do an MBA after gaining 5 years 
# experience anyway. What is the value today of his 5-year salary assuming that the 
# interest rate is 3%?
n = 5
r = 0.03
c = 25000
ans << pv(c, n, r).round

# Question 5
# (10 points) Rachna is considering a life insurance plan that will require her to 
# pay a premium of $200 every year for the next 40 years. She wants to make sure 
# that she is able to make this payment and wants to put away a lump sum today in 
# her bank to cover all future payments. How much would she need to deposit in her 
# bank if the annual interest rate on her deposit account is 4%? 
c = 200
n = 40
r = 0.04
ans << pv(c, n, r).round

# Question 6
# (10 points) Roxanne is in the market for a new house, and she has found a house 
# she likes that is selling for $250,000. The down payment on the house is 20% (the 
# amount that the bank should require you to pay in cash) and Roxanne plans to finance
# the remainder with a fixed rate mortgage. The annual rate is 6% and the mortgage is
# for 15 years, though payments are monthly. What is the interest component of Roxanne's
# first monthly payment? 
loan = 0.8 * 250000
r = 0.06/12
ans << (loan * r).round

# Question 7
# (15 points) Baako has invested $75,000 in a trust fund at 9% for his child's college 
# education. His child will draw $30,000 per year for four years, starting at the end 
# of year 7. What will be the amount that will be left over in the education fund at 
# the end of year 10, just after the child has withdrawn the fourth time? 
r = 0.09
investment_10 = comp(75000, 10, r)
education = fv(30000, 4, r)
remainder = investment_10 - education
ans << remainder.round

# Question 8
# (15 points) Two years ago Abilia purchased a $10,000 car; she paid $2000 down and 
# borrowed the rest. She took a fixed rate 60-month instalment loan at a stated rate
# of 8% per year. Interest rates have fallen during the last two years and she can 
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
 ans << "(yes, #{(p_8-p_6).round})"
else
 ans << "(no, #{(p_6-p_8).round})"
end 

# Question 9
# (15 points) Two years ago, you purchased a $20,000 car, putting $4,000 down and 
# borrowing the rest. Your loan was a 48-month fixed rate loan at a stated rate 
# of 6% per year.You paid a non-refundable application fee of $100 at that time 
# in cash. Interest rates have fallen during the last two years and a new bank 
# now offers to refinance your car by lending you the balance due at a stated rate
# of 4% per year. You will use the proceeds of this loan to pay off the old loan. 
# Suppose the new loan requires a $200 non-refundable application fee. Given all 
# this information, should you refinance? How much do you gain/lose if you do? 
loan = 20000 - 4000
r = 0.06/12
n = 48
payment = pmt(loan, n, r)
remaining_balance = pv(payment, n/2, r)
new_price = remaining_balance + 200
r_new = 0.04/12 
old_price = pv(payment, n/2, r_new)
if (new_price < old_price)
 ans << "(yes, gain #{(old_price - new_price).round})"
else
 ans << "(no, lose #{(new_price - old_price).round})"
end

# Question 10
# (15 points) You have just started your first job and you want to have the basic 
# appliances (fridge, washer, dryer, etc.) in your apartment. You face the 
# following choices: (i) Purchase all appliances at the store using a bank loan. 
# There is no down payment as the bank can take your appliances if you default on 
# the loan. The loan is at the annual market rate of 5%, and the loan amount is 
# $6,000 to be repaid monthly over 4 years.(ii) Rent-to-buy from the same store. 
# The monthly rental is $125 for 48 months and then you pay $1,000 to own all the 
# appliances. What is the net cost today of the cheapest option? 
rate = 0.05/12
option_1 = 6000
option_2 = pv(125, 48, rate) + disc(1000, 48, rate)
ans << (option_1<option_2 ? option_1 : option_2).round

# Print answers from the ans array
(1..ans.count).each {|i| puts i.to_s + ". "+ ans[i-1].to_s}
