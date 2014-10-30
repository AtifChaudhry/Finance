#!/usr/bin/python

# import the basic finace functions
import finance_formulas as fi

# Collect answers in the ans array
ans = []

# Question 1
# (5 points) Becky needs another $1,200 in her vehicle fund to purchase the car she wants. Her 
# parents offer to loan her the money, but want to teach her about the time value of money. They 
# offer to have her repay the loan in the future using birthday and holiday money. They agree 
# that she will repay $450 at each of her next two birthdays and one holiday season. These events
# are 3, 6 and 15 months from now. Assume a 6% cost of capital. Assume there is no risk of 
# default, and that compounding is monthly. What is the NPV of the loan?

r = 0.06/12
npv = -1200 + fi.disc(450, 3, r) + fi.disc(450, 6, r) + fi.disc(450, 15, r)

ans.append(fi.rnd(npv))

# Question 2
# (5 points) Jacob has an opportunity to invest in a new retail development in his building. The 
# initial investment is $50,000 and the expected cashflows are as follows: Year 1: $2,500 Year 2: 
# $5,000 Year 3: $5,000 Year 4: $7,500 Year 5: $10,000 Year 6: $10,000 Year 7: $15,000 Year 8: 
# $15,000 What is Jacob's IRR on this investment? (Enter the answer with no more nor less than 
# two decimal places, and leave off the % sign. For example, if your answer is 13.97% you should 
# enter it as 13.97 NOT 0.14 nor 14)

cf = [ 
 #     CF  # Year
   -50000, #    0
     2500, #    1
     5000, #    2
     5000, #    3
     7500, #    4
    10000, #    5
    10000, #    6
    15000, #    7
    15000  #    8
]
irr = fi.irr(cf)

ans.append(round(irr*100, 2))

# Question 3
# (5 points) Fabrice is looking to buy a new plug-in hybrid vehicle. The purchase price is $12,000
# more than a similar conventional model. However, he will receive a $7,500 federal tax credit 
# that he will realize at the end of the year. He estimates that he will save $1,200 per year in 
# gas over the conventional model; these cash outflows can be assumed to occur at the end of the 
# year. The cost of capital (or interest rate) for Fabrice is 6%. How long will Fabrice have to 
# own the vehicle to justify the additional expense over the conventional model?( i.e, What is the
# DISCOUNTED payback period in years? Discount future cash flows before calculating payback and 
# round to a whole year.)

ans.append("<Missing!>")

# Question 4
# (10 points) In high school Jeff often made money in the summer by mowing lawns in the 
# neighborhood. He just finished his freshman year of college and, after taking a Business 
# 101 class, he has some ideas about how to scale up his lawn mowing operation. Previously, 
# he had used his father's push mower, but he is thinking about getting a riding mower that 
# will save time and allow him to do more lawns. He found a used, zero turn, riding mower on 
# Craigslist for $1,200. He will also need a trailer to pull the mower behind his pickup; that 
# will cost him an additional $600. With the new mower he can take on an additional 20 lawns 
# per week at an average cash inflow of $20 per lawn he will receive at the end of each week. 
# He has 14 weeks of summer in which to mow lawns. (For convenience, assume that the mower and 
# trailer will have no value after Jeff is done with his work this summer.) The discount rate 
# for Jeff is 10% (Keep in mind this is an annual rate). What is the Net Present Value of the 
# mower/trailer project?

initial_investment = 1200+600
income_per_week    = 20*20 
weeks              = 14
r                  = 0.1/52
cf = [-initial_investment] + ([income_per_week] * weeks)
npv = fi.npv(cf, r)

ans.append(fi.rnd(npv))

# Question 5
# (10 points) Da Feng is looking to refinance his home because rates have gone down since he 
# purchased the house 5 years ago. He started with a 30-year fixed-rate mortgage of $240,000 at 
# an annual rate of 6.75%. He has to make monthly payments. He can now get a 25-year fixed-rate 
# mortgage at an annual rate of 5.5% on the remaining balance of his initial mortgage. This loan 
# also requires monthly payments. In order to re-finance, Da Feng will need to pay closing costs 
# of $4,500. These costs are out of pocket and cannot be rolled into the new mortgage. How much 
# will refinancing save Da Feng? (i.e. What is the NPV of the refinancing decision?)

balance_old = 240000
r_old       = 0.0675/12
n_old       = 30*12
pmt_old     = fi.pmt(balance_old, n_old, r_old)

n_new       = 25*12
r_new       = 0.055/12
balance_new = fi.pv(pmt_old, n_new, r_old)
cost_old    = fi.pv(pmt_old, n_new, r_new)
cost_new    = balance_new + 4500 # closing costs
savings     = cost_old - cost_new 

ans.append(fi.rnd(savings))

# Question 6
# (10 points) The United States purchased Alaska in 1867 for $7.2M (where M stands for million). 
# Assume that federal tax revenue from the state of Alaska (net federal expenditures) will be 
# $50M in 2012 and that tax revenue started in 1868 and has steadily increased by 3% annually 
# since then. Assume that the cost of capital (or interest rate) is 7%. What is the NPV of the 
# Alaska purchase? (Hint: Try and imagine you are in 1867 looking forward.)

n                 = 2012 - 1867
r                 = 0.07   # 7%/yr
purchase_price    = 7.2e6  # $7.2M
revenue_2012      = 50e6   # $50M
revenue_inflation = 0.03   # 3%/yr
revenue_stream    = [fi.disc(revenue_2012, x-1, revenue_inflation) for x in range(n,0,-1)] 
cf = [-purchase_price] + revenue_stream
npv = fi.npv(cf, r)

ans.append(fi.rnd(npv))

# Question 7
# (10 points) This question introduces you to the concept of an annuity with growth. The formula 
# is given on p.3, equation (7), of the Note on Formulae, but I would encourage you to try doing 
# it in Excel as well. (If the first cash flow is C, the next one will be C(1+g), and so on, 
# where g is the growth rate in cash flow). As an example, the present value of an annuity that 
# starts one year from now at $100, and grows at 5%, with the last cash flow in year 10, when the
# discount rate is 7%, is $860. Confirm this before attempting the problem; and use both the 
# formula and excel. What is the NPV of of a new software project that costs $1,000,000 today, 
# but has a cash flow of $200,000 in year 1 that grows at 3% per year till year 20? Similar
# investments earn 7.5% per year.

assert fi.rnd(fi.pv(100, 10, r=0.07, g=0.05)) == 860, "Confirmation failed!"

cost = 1e6   # $1,000,000
earn = 2e5   # $200,000/yr
g    = 0.03  # 3%/yr
r    = 0.075 # 7.5%/yr
n    = 20
npv  = -cost + fi.pv(earn, n, r, g)

ans.append(fi.rnd(npv))

# Question 8
# (15 points) Rebecca is 28 and considering going to graduate school so she sits down to 
# calculate whether it is worth the large sum of money. She knows that her first year tuition 
# will be $40,000, due at the beginning of the year (that is, right away). She estimates that 
# the 2nd year of tuition would be $42,000. She also estimates that her living expenses above 
# and beyond tuition will be $8,000 per year (assume this occurs at the end of the year) for the 
# first year and will increase to $9000 the next year. She expects to earn $18,000 for an 
# internship (Assume this inflow occurs one year from now). Were she to forgo graduate school she 
# would be able to make $55,000 at the end of this year and expects that to grow 3% annually. With
# a graduate degree, she estimates that she will earn $85,000/year after graduation, again with 
# annual 3% increases. Either way, she plans to work until 60 (she begins college right away). 
# The interest/discount rate is 6%. What is the NPV of her graduate education? (Note: All cash 
# flows except tuition payments occur at the end of the year.)

r                = 0.06      #6%/yr discount rate
current_age      = 28
retirement_age   = 60
working_years    = retirement_age - current_age
yearly_raise     = 0.03     # 3%/yr

# The PV of attending college
sal_college      = 85e3     # $85,000
college_duration = 2        # 2 years
college_costs_cf = [
 -40e3,                     # Tution = -$40,000
 -42e3 + -8e3 + 18e3,       # Tution = -$42,000 + Living Expenses = -$8,000 + Intership = $18,000 
 -9e3                       # Living Expenses = -$9,000
]
pv_college_cost  = fi.npv(college_costs_cf, r)
pv_college_earn  = fi.disc(fi.pv(sal_college, working_years-college_duration, r, yearly_raise), college_duration, r)
pv_college       = pv_college_cost + pv_college_earn

# The oppurtunity cost (i.e. the PV of skipping college)
sal_no_college   = 55e3     # $55,000
oppurtunity_cost = fi.pv(sal_no_college, working_years, r, yearly_raise)

# The NPV of attending college
npv              = pv_college - oppurtunity_cost

ans.append(fi.rnd(npv))

# Question 9
# (15 points) Reggie has just taken over management of a family business. He wants to make sure 
# that it makes financial sense to keep the business going. He could sell the building today for 
# $520,000. Keeping the business going will require a $50,000 renovation now and will yield an
# annual profit of $72,000 for the next 20 years (for simplicity assume these occur at year end, 
# beginning one year from now). The discount/interest rate is 10%? What are the NPV and IRR of 
# this decision?

r          = 0.1   # 10%/yr discount rate
value      = 520e3 # $520,000
renovation = 50e3  # $50,000
cost       = value + renovation
profit     = 72e3  # $72,000/yr
n          = 20    # 20 years
cf         = [-cost] + ([profit] * n)
npv        = fi.npv(cf, r)
irr        = fi.irr(cf)

ans.append("(%d; %.2f%%)" % (fi.rnd(npv), round(irr*100, 2)))

# Question 10
# (15 points) Sairah purchased an investment property for $350,000, 3 years ago. The after-tax 
# cashfow of the property has been $35,000 per year to date, but market conditions have improved 
# and Sairah expects the cashflow to improve to $42,000 per year for the next 25 years (assume 
# these are year end cashflows). The annual cost of capital (or cap rate) for this area is 9%. 
# What is the value of the property today?

# Approach:
#  Setup a single cashflow (starting with purchase price, 3 years of 
#  cash flow, and the 25 years of higher cash flows) and then compute 
#  the npv of that cf. Finally, move that npv forward three years to 
#  today.
r              = 0.09             # 9%/yr => cap. rate
purchase_price = 350e3            # $350,000
n_init         = 3                # 3 years at low return
n_rest         = 25               # 25 years at high return
return_init    = 35e3             # $35,000/yr
return_rest    = 42e3             # $42,000/yr
cash_flow_init = [return_init] * n_init  
cash_flow_rest = [return_rest] * n_rest  
cf             = [-purchase_price] + cash_flow_init + cash_flow_rest
npv            = fi.npv(cf, r)
npv_today      = fi.comp(npv, n_init, r)

ans.append(fi.rnd(npv_today))

# Print answers from the ans array
fi.print_lines(ans)
