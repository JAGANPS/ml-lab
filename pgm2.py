# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:01:24 2019

@author: ADMIN
"""

from sklearn.cluster import KMeans
#from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("km1.csv")
df1=pd.DataFrame(data)
print(df1)
f1=df1['Distance_Feature'].values
f2=df1['Speeding_Feature'].values
x=np.matrix(list(zip(f1,f2)))
plt.plot()
plt.xlim([0,100])
plt.ylim([0,50])
plt.title('dataset')
plt.ylabel('Speeding_Feature')
plt.xlabel('Distance_Feature')
plt.scatter(f1,f2)
plt.show()

#create new plot and data
plt.plot()
colors=['b','g','r']
markers=['o','v','s']

#kmeans Algorithm
#k=3
KMeans_model=KMeans(n_clusters=3).fit(x)
plt.plot()
for i,l in enumerate(KMeans_model.labels_):
    plt.plot(f1[i],f2[i],color=colors[l],marker=markers[l],ls='None')
    plt.xlim([0,100])
    plt.ylim([0,50])
plt.show()