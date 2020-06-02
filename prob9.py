import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    if(x>3 and x<7):
        return 1.0
    else:
        return 1e-19
def q():
    return np.random.standard_normal()

n=1000
x=3.0
arr=[]
chain=[]
narr=np.zeros(n)
for i in range(n):
    xp=x+q()
    r=np.random.rand()
    chain.append(xp)
    narr[i]=i
    if (fun(xp)/fun(x)) > r :
        x=xp
        
    if(x>3 and x<7):
        arr.append(x)
#print(arr)
b=20

bins=plt.hist(arr,b, density='true', histtype='bar',ec='white', label='Hist density')[1]

uni=np.ones(bins.size)*0.25
plt.plot(bins,uni,'g--',label='Uniform pdf')
plt.legend()
plt.show()



###########the chain
#print(np.amax(chain))
plt.scatter(narr,chain)
axes = plt.gca()
#axes.set_xlim([xmin,xmax])
axes.set_ylim([np.amin(chain),np.amax(chain)])
plt.plot(arr,color='red')
plt.title('Markov chain ')
plt.xlabel('steps n')
#plt.legend()
plt.show()



        
        
    
