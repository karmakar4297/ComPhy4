import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt

#Fisrt set
score=np.linspace(2,12,11)
probs=np.array([1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36])
obs1=np.array([4,10,10,13,20,18,18,11,13,14,13])
n1=np.sum(obs1)
tr1=probs*n1

#chi
V1=0
for i in range(obs1.size):
    V1=V1+((obs1[i]-tr1[i])**2)/(tr1[i])
PV1=1.0-scipy.stats.chi2.cdf(V1,obs1.size-1)

if(PV1<=0.01 or PV1>0.99):
    print('Set 1 : Not Sufficiently Random')
if(PV1<=0.05 and PV1>0.01 or PV1<=0.99 and PV1>0.95):
    print('Set 1 : Suspect')
if(PV1<=0.1 and PV1>0.05 or PV1<=0.95 and PV1>0.90):
    print('Set 1 : Almost Suspect')
if(PV1<=0.9 and PV1>0.1):
    print('Set 1 : Sufficiently Random')
    

#Second set
obs2=np.array([3,7,11,15,19,24,21,17,13,9,5])
n2=np.sum(obs2)
tr2=probs*n2

#chi
V2=0
for i in range(obs2.size):
    V2=V2+((obs2[i]-tr2[i])**2)/(tr2[i])
PV2=1.0-scipy.stats.chi2.cdf(V2,obs2.size-1)

if(PV2<=0.01 or PV2>0.99):
    print('Set 2 : Not Sufficiently Random')
if(PV2<=0.05 and PV2>0.01 or PV2<=0.99 and PV2>0.95):
    print('Set 2 : Suspect')
if(PV2<=0.1 and PV2>0.05 or PV2<=0.95 and PV2>0.90):
    print('Set 2 : Almost Suspect')
if(PV2<=0.9 and PV2>0.1):
    print('Set 2 : Sufficiently Random')


