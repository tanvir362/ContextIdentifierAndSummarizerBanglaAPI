import codecs

import pandas as pd
import joblib
import tanvir_stemming
import summarizer


def testModel():
    df = pd.read_csv("word_weights.csv")
    distinctwords = df['word']
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

model = joblib.load('contextIdentifierBangla.pkl')

#save mode for later use
#joblib.dump(model, 'contextIdentifierBangla.pkl')
testModel()
#print("Hello model")
