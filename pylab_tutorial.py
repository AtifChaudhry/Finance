#!/usr/bin/python

import pylab
import random

max    =    100
trials = 100000
freq = [0 for _ in range(max)]
for i in range(trials):
    freq[random.randrange(max)] += 1

pylab.plot(range(100), freq)
pylab.title("Random Trial")
pylab.xlabel("Value")
pylab.ylabel("Frequency")
pylab.show()
