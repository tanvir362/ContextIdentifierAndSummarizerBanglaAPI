import codecs

import pandas as pd
from sklearn import metrics
from sklearn import svm
import joblib
from sklearn.model_selection import train_test_split
import tanvir_stemming
import summarizer


def testModel():
    f = codecs.open("input.txt", "r", "utf8")
    inputdata = f.read()
    rwdata = inputdata
    rwdata = rwdata.splitlines()
    inputdata = tanvir_stemming.prepare_input(inputdata)
    #print(inputdata)
    testdata = []
    #constructing list of feature vector from input data
    for i in inputdata:
        pg = [0] * 4 #making list of size 4, contins 0 in each cell
        k = 0
        #feature vector for a paragraph
        for j in distinctwords:
            if j in i:
                cnt = i.count(j)
                pg[0] = pg[0] + cnt*df.at[k, 'politics']
                pg[1] = pg[1] + cnt*df.at[k, 'religious']
                pg[2] = pg[2] + cnt*df.at[k, 'sports']
                pg[3] = pg[3] + cnt*df.at[k, 'entertainment']
            k = k+1
        testdata.append(pg)
    #predict and print result 
    res = model.predict(testdata)
    indxrw = 0
    for i in res:
        if i == 100:
            print("politics")
            print("অনুচ্ছেদ")
            print(rwdata[indxrw])
            print("সারাংশ")
            print(summarizer.summary('politics', rwdata[indxrw]))
        elif i == 200:
            print("religious")
            print("অনুচ্ছেদ")
            print(rwdata[indxrw])
            print("সারাংশ")
            print(summarizer.summary('religious', rwdata[indxrw]))
        elif i == 300:
            print("sports")
            print("অনুচ্ছেদ")
            print(rwdata[indxrw])
            print("সারাংশ")
            print(summarizer.summary('sports', rwdata[indxrw]))
        else:
            print("entertainment")
            print("অনুচ্ছেদ")
            print(rwdata[indxrw])
            print("সারাংশ")
            print(summarizer.summary('entertainment', rwdata[indxrw]))
        indxrw = indxrw + 1


df = pd.read_csv("train_data/word_weights.csv")
distinctwords = df['word']

f = codecs.open("train_data/politics.txt", "r", "utf8")
politicsdata = f.read()
#print(politicsdata)
    
f = codecs.open("train_data/religious.txt", "r", "utf8")
religiousdata = f.read()

f = codecs.open("train_data/sports.txt", "r", "utf8")
sportsdata = f.read()

f = codecs.open("train_data/entertainment.txt", "r", "utf8")
entertaindata = f.read()

politicsdata = politicsdata.splitlines()
religiousdata = religiousdata.splitlines()
sportsdata = sportsdata.splitlines()
entertaindata = entertaindata.splitlines()

traindata = []
trainlevel = []
for i in politicsdata:
    paragraph = [0] * 4 #making list of size 4, contins 0 in each cell
    k = 0
    #feature vector for a paragraph
    for j in distinctwords:
        if j in i:
            cnt = i.count(j)
            paragraph[0] = paragraph[0] + cnt*df.at[k, 'politics']
            paragraph[1] = paragraph[1] + cnt*df.at[k, 'religious']
            paragraph[2] = paragraph[2] + cnt*df.at[k, 'sports']
            paragraph[3] = paragraph[3] + cnt*df.at[k, 'entertainment']
        k = k+1
    trainlevel.append(100)
    traindata.append(paragraph)

for i in religiousdata:
    paragraph = [0] * 4 #making list of size 4, contins 0 in each cell
    k = 0
    #feature vector for a paragraph
    for j in distinctwords:
        if j in i:
            cnt = i.count(j)
            paragraph[0] = paragraph[0] + cnt*df.at[k, 'politics']
            paragraph[1] = paragraph[1] + cnt*df.at[k, 'religious']
            paragraph[2] = paragraph[2] + cnt*df.at[k, 'sports']
            paragraph[3] = paragraph[3] + cnt*df.at[k, 'entertainment']
        k = k+1
    trainlevel.append(200)
    traindata.append(paragraph)
    
for i in sportsdata:
    paragraph = [0] * 4 #making list of size 4, contins 0 in each cell
    k = 0
    #feature vector for a paragraph
    for j in distinctwords:
        if j in i:
            cnt = i.count(j)
            paragraph[0] = paragraph[0] + cnt*df.at[k, 'politics']
            paragraph[1] = paragraph[1] + cnt*df.at[k, 'religious']
            paragraph[2] = paragraph[2] + cnt*df.at[k, 'sports']
            paragraph[3] = paragraph[3] + cnt*df.at[k, 'entertainment']
        k = k+1
    trainlevel.append(300)
    traindata.append(paragraph)

for i in entertaindata:
    paragraph = [0] * 4 #making list of size 4, contins 0 in each cell
    k = 0
    #feature vector for a paragraph
    for j in distinctwords:
        if j in i:
            cnt = i.count(j)
            paragraph[0] = paragraph[0] + cnt*df.at[k, 'politics']
            paragraph[1] = paragraph[1] + cnt*df.at[k, 'religious']
            paragraph[2] = paragraph[2] + cnt*df.at[k, 'sports']
            paragraph[3] = paragraph[3] + cnt*df.at[k, 'entertainment']
        k = k+1
    trainlevel.append(400)
    traindata.append(paragraph)
    
X_train, X_test, y_train, y_test = train_test_split(traindata, trainlevel, test_size=0.4, random_state=109)
    
model = svm.SVC(kernel='linear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
#print(X_test)
#print(y_pred)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred, labels=[100], average=None))
print("Recall:", metrics.recall_score(y_test, y_pred, labels=[100], average=None))
#save mode for later use
joblib.dump(model, 'contextIdentifierBangla.pkl')
testModel()
#print("Hello model")


#print(model.predict([traindata[40]]))