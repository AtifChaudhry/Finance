#!/usr/bin/python

# import the basic finace functions
import finance_formulas as fi

# Collect answers in the ans array
ans = []

### Question 1
#### (5 points) Carlos goes to the bank to take out a personal loan. The stated annual 
#### interest rate is 12%, but interest is compounded monthly and he will make monthly 
#### payments. The effective annual interest rate (EAR) of the loan is less than 12%. 

ans.append("false")

### Question 2
#### (5 points) Gloria is 35 and trying to plan for retirement. She has put a budget
#### together and plans to save $4,800 per year, starting at the end of this year, 
#### in a retirement fund until she is 65. Assume that she can make 7% on her account. 
#### How much will she have for retirement at age 65? 

n = 65 - 35
r = 0.07
c = 4800

ans.append(fi.rnd(fi.fv(c, n, r)))

### Question 3
#### (5 points) Mohammad has just turned 21 and now has access to the money his parents 
#### have been putting away in an account for him since he was 5 years old. His mother 
#### has asked him to guess what his account is worth given that they have invested 
#### $1,000 every year in the account starting on his 5th birthday and have just made one. 
#### The interest rate on the account has been 3.5% annually. 
#### How much is Mohammad's account worth today? 

n = 21 - 5 + 1
r = 0.035
c = 1000

ans.append(fi.rnd(fi.fv(c, n, r)))

### Question 4
#### (5 points) Marcel has just graduated from college and has found a job that will pay 
#### him $25,000 per year at the end of each year, but the job is only for 5 years. 
#### He is not worried about that because he plans to do an MBA after gaining 5 years 
#### experience anyway. What is the value today of his 5-year salary assuming that the 
#### interest rate is 3%?

n = 5
r = 0.03
c = 25000

ans.append(fi.rnd(fi.pv(c, n, r)))

### Question 5
#### (10 points) Rachna is considering a life insurance plan that will require her to 
#### pay a premium of $200 every year for the next 40 years. She wants to make sure 
#### that she is able to make this payment and wants to put away a lump sum today in 
#### her bank to cover all future payments. How much would she need to deposit in her 
#### bank if the annual interest rate on her deposit account is 4%? 

c = 200
n = 40
r = 0.04

ans.append(fi.rnd(fi.pv(c, n, r)))

### Question 6
#### (10 points) Roxanne is in the market for a new house, and she has found a house 
#### she likes that is selling for $250,000. The down payment on the house is 20% (the 
#### amount that the bank should require you to pay in cash) and Roxanne plans to finance
#### the remainder with a fixed rate mortgage. The annual rate is 6% and the mortgage is
#### for 15 years, though payments are monthly. What is the interest component of Roxanne's
#### first monthly payment? 

loan = 0.8 * 250000
r    = 0.06/12

ans.append(fi.rnd(loan * r))

### Question 7
#### (15 points) Baako has invested $75,000 in a trust fund at 9% for his child's college 
#### education. His child will draw $30,000 per year for four years, starting at the end 
#### of year 7. What will be the amount that will be left over in the education fund at 
#### the end of year 10, just after the child has withdrawn the fourth time? 

r = 0.09
investment = fi.comp(75000, 10, r)
education  = fi.fv(30000, 4, r)

ans.append(fi.rnd(investment - education))

### Question 8
#### (15 points) Two years ago Abilia purchased a $10,000 car; she paid $2000 down and 
#### borrowed the rest. She took a fixed rate 60-month instalment loan at a stated rate
#### of 8% per year. Interest rates have fallen during the last two years and she can 
#### refinance her car by borrowing the amount she still owes on the car at a new 
#### fixed rate of 6% per year for 3 years. Should Abilia refinance her loan? How 
#### much will she save per month for the next three years if she decides to 
#### refinance?

bal = 10000 - 2000
r_8 = 0.08/12
n_8 = 60
p_8 = fi.pmt(bal, n_8, r_8)
n_6 = 3*12
bal = fi.pv(p_8, n_6, r_8)
r_6 = 0.06/12
p_6 = fi.pmt(bal, n_6, r_6)

if (p_6 < p_8):
 ans.append("(yes, %s)" % str(fi.rnd(p_8-p_6)))
else:
 ans.append("(no, %s)"  % str(fi.rnd(p_6-p_8)))

### Question 9
#### (15 points) Two years ago, you purchased a $20,000 car, putting $4,000 down and 
#### borrowing the rest. Your loan was a 48-month fixed rate loan at a stated rate 
#### of 6% per year.You paid a non-refundable application fee of $100 at that time 
#### in cash. Interest rates have fallen during the last two years and a new bank 
#### now offers to refinance your car by lending you the balance due at a stated rate
#### of 4% per year. You will use the proceeds of this loan to pay off the old loan. 
#### Suppose the new loan requires a $200 non-refundable application fee. Given all 
#### this information, should you refinance? How much do you gain/lose if you do? 

loan      = 20000 - 4000
r         = 0.06/12
n         = 48
payment   = fi.pmt(loan, n, r)
balance   = fi.pv(payment, n/2, r)
new_price = balance + 200
r_new     = 0.04/12 
old_price = fi.pv(payment, n/2, r_new)

if (new_price < old_price):
 ans.append("(yes, gain %s)" % str(fi.rnd(old_price - new_price)))
else:
 ans.append("(no, lose %s)"  % str(fi.rnd(new_price - old_price)))

### Question 10
#### (15 points) You have just started your first job and you want to have the basic 
#### appliances (fridge, washer, dryer, etc.) in your apartment. You face the 
#### following choices: (i) Purchase all appliances at the store using a bank loan. 
#### There is no down payment as the bank can take your appliances if you default on 
#### the loan. The loan is at the annual market rate of 5%, and the loan amount is 
#### $6,000 to be repaid monthly over 4 years.(ii) Rent-to-buy from the same store. 
#### The monthly rental is $125 for 48 months and then you pay $1,000 to own all the 
#### appliances. What is the net cost today of the cheapest option? 

rate     = 0.05/12
option_1 = 6000
option_2 = fi.pv(125, 48, rate) + fi.disc(1000, 48, rate)

ans.append(fi.rnd(option_1 if (option_1 < option_2) else option_2))

### Extra HW Question
#### (15 points) You are interested in a new Ford Taurus. After visiting your Ford dealer, 
#### doing your research on the best leases available, you have three options. (i) Purchase 
#### the car for cash and receive a $1,500 cash rebate from Dealer A. The price of the car is 
#### $15,000. (ii) Lease the car from Dealer B. Under this option, you pay the dealer $500 now 
#### and $200 a month for each of the next 36 months (the first $200 payment occurs 1 month 
#### from today). After 36 months you may buy the car for $8,000. (iii) Purchase the car from 
#### Dealer C who will lend you the entire purchase price of the car for a zero interest 
#### 36-month loan with monthly payments. The car price is $15,000. Suppose the market interest 
#### rate is 6%. What is the net cost today of the cheapest option? 

# Market interest rate (monthly) and loan duration (months)
r = 0.06/12
n = 36

# Option (i)
sticker_price   = 15000
discount        = 1500
option_1        = sticker_price - discount

# Option (ii)
down_payment    = 500
lease_payment   = 200
residual        = 8000
option_2        = down_payment + fi.pv(lease_payment, n, r) + fi.disc(residual, n, r)

# Option (iii)
sticker_price   = 15000
monthly_payment = sticker_price/n
option_3        = fi.pv(monthly_payment, n, r)

if (option_1 < option_2 and option_1 < option_3):
  ans.append("Option 1 (Dealer A): %s" % fi.rnd(option_1))
elif (option_2 < option_3):
  ans.append("Option 2 (Dealer B): %s" % fi.rnd(option_2))
else:
  ans.append("Option 3 (Dealer C): %s" % fi.rnd(option_3))

### Class Problem
#### Suppose you are exactly 30 years old. You believe that you will be able to save for
#### the next 20 years, until you are 50. For 10 years following that, and till your 
#### retirement at age 60, you will have a spike in expenses and you will not be
#### able to save. If you want to guarantee yourself $8000 per month starting one month 
#### after your 60th birthday, how much should you save every month, for the next 20 years
#### starting at the end of next month. Assume your investments are expected to yield 8%
#### annually and you are likely to live till 80.

r                = 0.08/12
expenses         = fi.disc(fi.pv(8000, (80-60)*12, r), (60-30)*12, r)
saving_per_month = fi.pmt(expenses, (50-30)*12, r)

ans.append(fi.rnd(saving_per_month))
 
# Print answers from the ans array
fi.print_lines(ans)

