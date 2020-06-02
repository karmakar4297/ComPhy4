
import numpy as np
import matplotlib.pyplot as plt
n=10000
x1=np.random.rand(n)
x2=np.random.rand(n)
y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)
b=30

plt.hist(y1,b,density='true',histtype='bar', ec='white', label = 'Hist.')

pdf1=(1/(np.sqrt(np.pi*2)))*np.exp(-y1**2/2)
plt.plot(y1[np.argsort(y1)],pdf1[np.argsort(y1)],'g--',label='pdf')

##For y2 as well we will get Gaussian dist.

plt.legend(loc='upper right')
plt.title('Gaussian using Box Muller')
plt.show()
