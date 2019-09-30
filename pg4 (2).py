from numpy import *
import operator
from os import listdir
import matplotlib.pyplot as plt
import pandas as pd
import numpy as npl
import numpy.linalg as np
from scipy.stats.stats import pearsonr
def kernel(point,xmat,k):
    m,n=npl.shape(xmat)
    weights=npl.mat(npl.eye((m)))
    for j in range(m):
        diff=point-x[j]
        weights[j,j]=npl.exp(diff*diff.T/(-2.0*k**2))
        return weights
def localweight(point,xmat,ymat,k):
    wei=kernel(point,xmat,k)

    W=(x.T*(wei*x)).I*(x.T*(wei*ymat.T))
    return W
def localWeightRegression(xmat,ymat,k):
    m,n=npl.shape(xmat)
    ypred=npl.zeros(m)
    for i in range(m):
        ypred[i]=xmat[i]*localweight(xmat[i],xmat,ymat,k)
    return ypred
data=pd.read_csv('10data.csv')
bill=npl.array(data.total_bill)
tip=npl.array(data.tip)
mbill=npl.mat(bill)
mtip=npl.mat(tip)
m=npl.shape(mbill)[1]
one=npl.mat(npl.ones(m))
x=npl.hstack((one.T,mbill.T))
ypred=localWeightRegression(x,mtip,2)
SortIndex=x[:,1].argsort(0)
xsort=x[SortIndex][:,0]
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(bill,tip,color='green')
ax.plot(xsort[:,1],ypred[SortIndex],color='red',lineWidth=5)
plt.xlabel('total bill')
plt.ylabel('tip')
plt.show();
        
        