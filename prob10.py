import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner
import csv

def log_likelihood(theta, x, y, yerr):
    a, b, c = theta
    model = a*x*x + b*x + c
    sigma2 = yerr**2
    # actually negative ln L
    return 0.5*np.sum((y - model)**2/sigma2+np.log(2 * np.pi * sigma2))

def log_prior(theta):
    a, b, c = theta
    if -250<a<250 and -500.0 < b < 500 and 0.0 < b < 1000.0:
        return 0.0
    return -np.inf


def log_probability(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp - log_likelihood(theta, x, y, yerr)

def model(coeff,x):
    a,b,c=coeff
    return a*x**2+b*x+c


index=[]
x=[]
y=[]
yerr=[]
with open('data.txt', 'r') as file:
    data=csv.reader(file, delimiter='&')
    for c in data:
        index.append(float(c[0]))
        x.append(float(c[1]))
        y.append(float(c[2]))
        yerr.append(float(c[3]))
    

x=np.array(x)
y=np.array(y)
yerr=np.array(yerr)
guess = (1.0, 1.0, 1.0)

soln = minimize(log_likelihood, guess, args=(x, y, yerr))

nwalkers, ndim = 50, 3
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)


sampler = emcee.EnsembleSampler(nwalkers,ndim,log_probability, args=(x, y, yerr))
sampler.run_mcmc(pos, 4000)
samples = sampler.get_chain()
ready=sampler.get_chain(discard=200,thin=30,flat=True)


fig=plt.subplots(3)[0]

fig.suptitle('Markov chain for first 100 steps')
plt.subplot(3,1,1)
plt.plot(samples[1:100, :, 0]) # a values
plt.ylabel('a')
plt.subplot(3,1,2)
plt.plot(samples[1:100, :, 1]) # b values
plt.ylabel('b')
plt.subplot(3,1,3)
plt.plot(samples[1:100, :, 2]) # cvalues
plt.ylabel('c')





medians = np.median(ready, axis=0)

a_true,b_true,c_true=medians

fig = corner.corner(ready, labels=['a','b','c'],truths=[a_true, b_true,c_true])

print('The best fit parameters are: a =',a_true,'b =',b_true,'c =',c_true)

plt.figure()

xpts=np.linspace(np.amin(x),np.amax(x),100)
rand200=np.random.randint(len(ready),size=200)
for i in rand200:
    abc=ready[i]
    plt.plot(xpts,model(abc[:3],xpts),color='c')
plt.scatter(x,y,color='black',label='Given data')
plt.plot(xpts,model(medians,xpts),'r',label='Best fit')
plt.legend()
plt.show()
