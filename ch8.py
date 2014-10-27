#!/usr/bin/python

# import the basic finace functions
import basic as fin

# EG 9.1 The cash flows over a five year for a project will be
# $2000 for the first two years,  $4000 for the next two years,
# and $5000 in the last year. It will cost about $10000 to start
# the project. With a 10% discount rate, should we start this
# project?
cf  = [-10000, 2000, 2000, 4000, 4000, 5000]
r = 0.1
npv = fin.npv(cf, r)
print "The NPV is $%i, so %slaunch the project." % (npv, "don't " if npv < 0 else "")

# EG 9.7 Consider the two investments: Investment A: (-400, 250, 280) and 
# Investment B: (-500, 320, 340). What is the crossover rate (i.e. the 
# rate at which both have the same NPV).
inv_a = [-400, 250, 280]
inv_b = [-500, 320, 340]
print "crossover rate = %.2f" % round(fin.cxr(inv_a, inv_b), 2)
