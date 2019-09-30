
import pandas as pd
msg=pd.read_csv('lab6.txt',names=['message','label'])
print('The dimension of the dataset',msg.shape)
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
x=msg.message
y=msg.labelnum
print(x)
print(y)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y)
print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)

from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
xtrain_dtm=count_vect.fit_transform(xtrain)
xtest_dtm=count_vect.transform(xtest)
print(count_vect.get_feature_names())
df=pd.DataFrame(xtrain_dtm.toarray(),columns=count_vect.get_feature_names())
print(df)
print(xtrain_dtm)
from sklearn.naive_bayes import MultinomialNB
df=MultinomialNB().fit(xtrain_dtm,ytrain)
predicted=df.predict(xtest_dtm)

from sklearn import metrics
print('accuracy matrix')
print('accuracy of the classifier',metrics.accuracy_score(ytest,predicted))
print('confusion matrix')
print(metrics.confusion_matrix(ytest,predicted))
print('Recall & precision')
print(metrics.precision_score(ytest,predicted))

'''docs_new=['I like this place','My Boss is not my saviout']
   x_new_counts=count_vect.transform(docs_new)
   predictednew=clf.predict(x_new_counts)
   for doc,category in zip(docs_new,predictednew):
        print('%s->%s'%(doc,msg.Labelnum[category]))'''