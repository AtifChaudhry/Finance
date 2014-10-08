# A Cash Flow (CF) is represented as an array of numbers. For example, 
# the CF for an intial investment of $100, which pays $0 in the first 
# period, and then pays $150 in the second period will be: [-100, 0, 150]

# The rate of return (r) is represented as a float, for example the rate
# of 10% is represented as 0.1

# Net Present Value (npv) of a cashflow (cf) with an intial investement (c0)
# for a given rate of return (r).
def npv(r, c0, cf)
  cf.zip(1..cf.count).inject(c0) {|a,v| a+v[0]/((1.0+r)**v[1])}
end

npv(0.1, -1, [2]).round(2)
npv(0.1, -1, [0, 3]).round(2)
npv(0.1, -1, [1, 1, 1, 1, 1, 2]).round(2)
npv(0.1, -1, [0, 2, 0, 2, 0, 3]).round(2)

# Internal Rate of Return (IRR) of a CF
def IRR(cf)
end


