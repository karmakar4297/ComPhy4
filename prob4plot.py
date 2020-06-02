import numpy as np
import matplotlib.pyplot as plt
file=open('prob4out.txt','r')
data=np.loadtxt(file)
b=20
plt.hist(data, b, histtype='bar', ec='white', label='Hist of exp. dist. using C', density='true')
file.close()
xarr=np.linspace(0,np.amax(data),data.size)

pdf=2*np.exp(-2*xarr)
plt.plot(xarr,pdf, 'g--',label='exp. pdf')
#plt.hist(data, b, histtype='bar', ec='white', label='Hist of exp. dist.')
plt.legend(loc='upper right', frameon='False')
plt.title(r'$f(x)=2e^{-2x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

