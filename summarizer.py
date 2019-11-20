# -*- coding: UTF-8 -*-
import tanvir_stemming
import pandas as pd
import operator

#input paragraph(not cleaned) output sentence stem mapping
def sentence_stems_mapping(text="Tanvir ahmed"):
    delimiter = "।?!"
    temp = {}
    sentence = ""
    sentence_list = []
    indx = 0
    for i in text:
        sentence = sentence + i
        if i in delimiter:
            sentence_list.append(sentence)
            temp[indx] = tanvir_stemming.sentence_stemmer(sentence)
            sentence = ""
            indx = indx + 1

    return sentence_list, temp


#input: sentence stems mapping output: sentence score dictionary
def sentence_scoring(type, mdict):
    df = pd.read_csv("word_weights.csv")
    distinctwords = df['word']
    indx = 0
    indx_score = {}
    for key in mdict:
        k = 0
        score = 0
        for j in distinctwords:
            if j in mdict[key]:
                cnt = mdict[key].count(j)
                score = score + cnt * df.at[k, type]
            k = k + 1
        mdict[key] = score
    return mdict


#input paragraph without cleaning
def summary(type, paragraph):
    sentence_list, dict = sentence_stems_mapping(" "+paragraph) #assigns sentence list of the paragraph and inxex vs stem dictionary
    scored_sentence = sentence_scoring(type, dict)
    sorted_d = sorted(scored_sentence.items(), key=operator.itemgetter(1))
    #print(sorted_d)
    #finding more scored 3 scentance's position
    indxes = []
    j = 0
    for i in sorted_d:
        indxes.append(i[0])
        j = j + 1
        if j == 3:
            break

    indxes.sort()
    #print(indxes)
    summ = ""
    for i in indxes:
        summ = summ + sentence_list[i]
    return summ

#s = summary("বিএনপিকে রাজনীতি করতে দেয়া হচ্ছে না অভিযোগ করে ড. খন্দকার মোশাররফ হোসেন বলেন, আমরা দলকে পুনর্গঠনের জন্য দলকে জেলা ও উপজেলা পর্যায়ে সুসংগঠিত করছি। এ জন্য যে কাউন্সিল করা দরকার সেই কাউন্সিল করতে অনুমতি দেয়া হচ্ছে না। আমরা আমাদের দলে, অঙ্গ ও সহযোগী সংগঠনে গণতান্ত্রিক প্রক্রিয়া চালু করতে চেষ্টা করছি। সেই চেষ্টাকেও আজকে সরকার নানাভাবে বাধাগ্রস্ত করছে। আপনারা দেখেছেন, ১৪ সেপ্টেম্বর ছাত্রদলের কাউন্সিল হওয়ার কথা ছিল। সেটিও বন্ধ করতে কোর্ট থেকে নিষেধাজ্ঞা জারি করা হয়েছে।")
#print(s)



