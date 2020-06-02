import numpy as np
import matplotlib.pyplot as plt
import time

a=7382047  # These values are taken for example.
c=234819763
m=932485873
x=1

n=10000
start=time.time()
randarr=np.zeros(n)
for i in range(n):
    x=(a*x+c)%m
    randarr[i]=x/m
end=time.time()
file=open('prob3out.txt','a')
file.write('\n Time (in sec.) taken to produce 10 k uniform deviates with linear cong:  ')
file.write(str(end-start))
file.close()
    
b=20
uniform=np.ones(n)
plt.plot(randarr[np.argsort(randarr)],uniform, 'g--',label='Uniform pdf')
plt.hist(randarr, b, density='true', histtype='bar', ec='white', label='From lenear cong.')
plt.xlabel(x)
plt.legend(loc='lower right', frameon='False')
plt.show()
