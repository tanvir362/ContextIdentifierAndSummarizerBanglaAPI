import codecs

import pandas as pd
import joblib
import tanvir_stemming
import summarizer


def getresult(inputdata):
    model = joblib.load('contextIdentifierBangla.pkl')
    df = pd.read_csv("word_weights.csv")
    distinctwords = df['word']

    rwdata = inputdata
    rwdata = rwdata.splitlines()
    inputdata = tanvir_stemming.prepare_input(inputdata)
    #print(inputdata)
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
    resultes = []  # added for store result dict
    for i in res:
        result = {}
        if i == 100:
            result["paragraph"] = rwdata[indxrw]
            result["category"] = "politics"
            result["summary"] = summarizer.summary('politics', rwdata[indxrw])
        elif i == 200:
            result["paragraph"] = rwdata[indxrw]
            result["category"] = "religious"
            result["summary"] = summarizer.summary('politics', rwdata[indxrw])
        elif i == 300:
            result["paragraph"] = rwdata[indxrw]
            result["category"] = "sports"
            result["summary"] = summarizer.summary('politics', rwdata[indxrw])
        else:
            result["paragraph"] = rwdata[indxrw]
            result["category"] = "entertainment"
            result["summary"] = summarizer.summary('politics', rwdata[indxrw])
        resultes.append(result)
        #print(result)
        indxrw = indxrw + 1
    #print(resultes)
    return {"results": resultes}

