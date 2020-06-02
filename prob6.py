import numpy as np
import matplotlib.pyplot as plt
def fun(x):
    return np.sqrt(2/np.pi)*np.exp(-x**2/2)
n=10000
x=np.random.rand(n)*10
#xneg=np.random.rand(n)*(-10)
#x=np.append(xneg,xpos)
#print(x)
y=np.random.rand(n)
good=np.zeros(1, dtype=float)
pdf=np.sqrt(2/np.pi)*np.exp(-x**2/2)

for i in range(n):
    temp=fun(x[i])
    if(y[i]<=temp):
        if(i==0):
            good[i]=x[i]
        else:
            good=np.append(good,x[i])
b=10

plt.hist(good,b,density='true', histtype='bar', ec='white', label='Using rejection method')
#plt.scatter(x,y)
plt.plot(x[np.argsort(x)],pdf[np.argsort(x)], 'g--', label='pdf')
axes = plt.gca()
axes.set_xlim([0,5])
plt.title(r'$f(x)=\sqrt{\frac{2}{\pi}}\exp(\frac{-x^2}{2})$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
    
