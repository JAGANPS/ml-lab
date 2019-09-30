# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:24:15 2019

@author: ADMIN
"""
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import datasets
iris=datasets.load_iris()
iris_data=iris.data
iris_labels=iris.target
print(iris_data)
print(iris_labels)
x_train,x_test,y_train,y_test=train_test_split(iris_data,iris_labels,test_size=0.30)
Classifier=KNeighborsClassifier(n_neighbors=5)
Classifier.fit(x_train,y_train)
y_pred=Classifier.predict(x_test)
print(confusion_matrix(y_test,y_pred))
print('accuracy metrics')
print(classification_report(y_test,y_pred))
