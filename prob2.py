import numpy as np
import matplotlib.pyplot as plt
import time
start=time.time()
x=np.random.rand(10000)
end=time.time()
file=open('prob3out.txt','a')
file.write('\n Time (in sec.) taken to produce 10 k uniform deviates with np.random.rand:  ')
file.write(str(end-start))
file.close()
pdf=np.ones(x.size)
b=20
plt.hist(x,b,density='true',histtype='bar',ec='white',label='Using np.random.rand()')
plt.plot(x[np.argsort(x)],pdf,'g--',label='Uniform pdf')
plt.xlabel('x')
plt.legend(loc='lower right')
plt.show()

