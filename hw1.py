#!/usr/bin/python

# import the basic finace functions
from basic import *

# Collect answers in the ans array
ans = []

# Question 1
# (5 points) $50 today is worth MORE than $50 tomorrow.
ans.append("true")

# Question 2
# (5 points) At an interest rate of 10% it is better to have $100 today than $120 in 2 years.
ans.append("true" if 100 > disc(c=120, n=2, r=0.1) else "false")

# Question 3
# (5 points) Megan wants to buy a designer handbag and plans to earn the money babysitting. 
# Suppose the interest rate is 6% and she is willing to wait one year to purchase the bag. 
# How much babysitting money (to the nearest whole dollar) will she need to earn today to 
# buy the bag for $400 one year from now?
ans.append(rnd(disc(c=400, n=1, r=0.06)))

# Question 4
# (10 points) Johnny and Darren both earn $100 working on their respective neighbors' big 
# farms. Johnny puts his $100 in the piggy bank that his parents gave him to encourage him 
# to save. Darren puts his money in a savings account his parents set up for him. The 
# savings account pays 3% interest. They both take their money out after 5 years. How much 
# more money does Darren have than Johnny?
johnny = 100
darren = comp(c=100, n=5, r=0.03)
ans.append(rnd(darren - johnny))

# Question 5
# (10 points) Don has just received a cash gift of $50,000 from his rich eccentric uncle. 
# He wants to set it aside to pay for his daughter Cynthia's college education. Cynthia 
# will begin college in 10 years and Don's financial advisor says that she can earn 7% 
# interest on an investment in a special college fund. How much will Don have in the fund 
# when Cynthia begins college? 
ans.append(rnd(comp(c=50000, n=10, r=0.07)))

# Question 6
# (10 points) Bridgette's grandparents opened a savings account for her and placed $500 
# in the account. The account pays 3.5% interest. Bridgette wants to be a singer and she 
# has her heart set on a new karaoke machine. The machine costs $150. How much less will 
# the account be worth in 8 years if she buys the karaoke machine now versus leaving the 
# account untouched? 
ans.append(rnd(comp(c=150, n=8, r=0.035)))

# Question 7
# (10 points) The Johnson family is worried about their ability to pay college tuition 
# for their daughter Chloe. Tuition rates are currently $9,500 per year at the state 
# college and have been increasing at a rate of 7% annually. Chloe will begin college 
# in 7 years. The Johnson's have $9,500 set aside now in a college plan that will earn 
# 6% per year. They recently heard about a plan to pre-pay tuition at current rates, 
# that is pay $9,500 per year of college. Should they pre-pay Chloe's first year now 
# or keep the money invested and pay the tuition 7 years from now? How much are they 
# saving in FV terms with this decision?
tution_future = comp(c=9500, n=7, r=0.07)
saving_future = comp(c=9500, n=7, r=0.06)
ans.append("Pre-pay; %i" % rnd(tution_future - saving_future))

# Question 8
# (15 points) Juan has $100,000 to invest and he has narrowed down his decision to 
# two investments. Option A returns 60% annually for 4 years, but the maximum investment 
# he can make is $10,000. Option B returns 12% annually for 4 years and would require 
# the entire $100,000. Which option produces the best result for Juan and what is the 
# benefit over the lesser option? Assume that the $90,000 not invested in Option A 
# would be placed in a safe deposit box earning no interest.
option_a = comp(c=10000, n=4, r=0.6) + 90000
option_b = comp(c=100000, n=4, r=0.12)
ans.append("Option %s; %i" % (("A" if option_a > option_b else "B"), rnd(abs(option_a - option_b))))
 
# Question 9
# (15 points) Jessica is in the market for a new car. She has narrowed her search down 
# to 2 models. Model A costs $20,000 and Model B costs $18,000. With both cars she plans 
# to pay cash and own them for 5 years before trading in for a new car. Her research 
# indicates that the trade in value for Model A after 5 years is 50% of the initial 
# purchase price. The trade in value for Model B is 25%. Jessica has no emotional 
# attachment to either model and wants to make a strictly financial decision. The
# interest rate is 6%. For simplicity assume that operating and maintenance costs for 
# the models are identical every year. Which model is the better decision and how much 
# "cheaper" is it than the alternative?

n = 5
r = 0.06

# Model A
price_a  = 20000
resale_a = price_a * 0.5
cost_a   = price_a - disc(resale_a, n, r)

# Model B
price_b  = 18000
resale_b = price_b * 0.25
cost_b   = price_b - disc(resale_b, n, r)

ans.append("Model %s; %i" % (("A" if cost_a < cost_b else "B"), rnd(abs(cost_a - cost_b))))

# Question 10
# (15 points) Christine is a new homebuyer. She wants to make sure that she incorporates 
# the cost of maintenance into her decision. She estimates that routine repairs and 
# maintenance on the home she is considering will be $1,590 in the first year (one year
# from now). Due to the increasing age of the home, she expects that maintenance costs
# will increase 6% annually. The interest rate is 5%. If she plans to be in the home for
# 10 years, what is the present value of all future maintenance? (Note that maintenance
# costs will change annually, and starts one year from now and she plans to do the last
# one before selling her house.)

r             = 0.05
cost_inc_rate = 0.06
cost_initial  = 1590
cost_total    = 0
for i in range(10):
  cost_current = comp(cost_initial, i, cost_inc_rate)   
  cost_total  += disc(cost_current, i+1, r)
ans.append(rnd(cost_total))

# Print answers from the ans array
for i in range(len(ans)): print str(i+1) + ". " + str(ans[i])
