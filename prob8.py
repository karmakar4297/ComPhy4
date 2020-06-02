import numpy as np
def fun(x,y):
    return x**2+y**2
n=1000000
ax=-1
bx=1
ay=-1
by=1
x=np.random.uniform(ax,bx,n)
y=np.random.uniform(ay,by,n)
count=0
for i in range(n):
    temp=fun(x[i],y[i])
    if temp<=1:
        count=count+1
A=(count/n)*(bx-ax)*(by-ay)
print('Area of the circle: ',A)

########FOR 10-dim
def dfun(r):
    return np.matmul(np.transpose(r),r)
d=10
ar=-1
br=1
r=np.random.uniform(ar,br,(n,d))
#print(r[0])
count=0
for i in range(n):
    temp=dfun(r[i])
    #print(temp)
    if temp<=1:
        count=count+1
dA=(count/n)*(br-ar)**d
print('\nVolume of',d,'dim unit sphere: ',dA)


