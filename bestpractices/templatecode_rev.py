"""
This template code is intended to provide practice in debugging, speed 
optimization, and spotting bad habits in programming. The code runs but 
is deeply flawed. If you improve the code following all the best practices 
you know, you'll learn something about both programming and the Central 
Limit Theorem.

Author: Sheila Kannappan
Last modified: September 2019
"""

# standard imports and naming conventions; uncomment as needed
import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
import scipy.stats as stats     # statistical functions
#import pdb                      # python debugger
#import time                     # python timekeeper

def gaussfunc(xvals, mean, sigma):
    yvals = np.exp(-1.*(((xvals-mean)/sigma)**2 / 2.)) # perform square once, y->yvals
    norm = 1./(np.sqrt(2. * np.pi) * sigma) # remove extra square operation
    prob = norm * yvals # use meaningful names
    return prob

def poissonfunc(xvals, mean):   # move function out of loop to top of code
    prob=stats.poisson.pmf(xvals, mean) # use array math instead of loop
    return prob # note that defining this function proved entirely unnecessary,
                # could just use "stats.poisson.pmf" instead of poissonfunc

def main():
    # rename single-letter variables U, N, n, y -- note that "n" is a command for pdb!
    Urate = 8. # underlying rate of gym users per hour 
    Nct = np.array([6, 36, 216, 1296]) # typical total number of people counted (powers of 6)
    nhr = Nct/Urate # time to count this many people
    # uncomment below to do array string operation
    labelarr = ["count for %s hr" % ihr for ihr in nhr]
    
    for i in range(0, len(Nct)):
        
        # plot probabilities of count values for range around mean
        # meaningful variable names -> readability (poissprob, gaussprob, ctvals)
        mean = Nct[i]
        maxval = 2*mean
        ctvals=np.arange(0, maxval)
        poissprob = poissonfunc(ctvals, mean)
        plt.plot(ctvals, poissprob, 'r', lw=3)
        sel = np.where(np.isclose(poissprob,max(poissprob)))
        sel=sel[0] #output of np.where gives indices in first entry of tuple
        ctvaltomark = np.mean(ctvals[sel]) # if ties in maxprob, take mean of ctvals values
        poissprobtomark = poissprob[sel[0]] # if ties in maxprob, just need one prob value
        plt.text(ctvaltomark, poissprobtomark, labelarr[i]) # use labelarr instead of looping over string operation
        # the lines below needed to be in the loop
        # plot Gaussian distribution with matching mean and sigma
        sigma=np.sqrt(mean)
        gaussprob = gaussfunc(ctvals, mean, sigma)
        plt.plot(ctvals, gaussprob, 'b')
    
    # these labels didn't need to be in the loop
    plt.xlabel("count value")
    plt.ylabel("probability")
    plt.xscale("log")
    plt.xlim([1,100])

if __name__ == '__main__':
    main()
    plt.show()
