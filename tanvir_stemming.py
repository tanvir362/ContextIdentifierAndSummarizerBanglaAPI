# -*- coding: UTF-8 -*-
import codecs
from bengali_stemmer.rafikamal2014 import RafiStemmer


#return string without punction
def punctuation_remover(text="tanvir"):
    punctuations = '''।‘’“”!()-[]{};:'"\,<>./?@#$%^&*_~'''

    temp = ""
    for i in text:
        if i not in punctuations:
            temp = temp + i
    return temp


#return list of word of given string without stop word
def stopword_remover(text="tanvir"):
    text = text.split()
    f = codecs.open("banglaStopWords.txt", "r", "utf8")
    stopWords = f.read()
    stopWords = stopWords.splitlines()

    temp = []
    for i in text:
        if i not in stopWords:
            temp.append(i)

    return temp


#return list of root word of given word list
def stemmer(words):
    steams = []
    stemmer = RafiStemmer()
    for i in words:
        steams.append(stemmer.stem_word(i))

    return steams


def steam_writer(paragraphs="tanvir", filename="mysteams.txt"):
    paragraphs = paragraphs.splitlines()
    line = ""
    for i in paragraphs:
        paragraph = punctuation_remover(i)
        paragraph = stopword_remover(paragraph)
        paragraph = stemmer(paragraph)
        for j in paragraph:
            line = line + j + " "
        line = line + '\n'
    f = open(filename, 'w', encoding="utf-8")
    f.write(line)


#input uncleaned read data return list of list of stem of every line
def prepare_input(inputs="tanvir"):
    inputs = inputs.splitlines()
    lines = []
    for i in inputs:
        paragraph = punctuation_remover(i)
        paragraph = stopword_remover(paragraph)
        paragraph = stemmer(paragraph)
        line = ""
        for j in paragraph:
            line = line + j + " "
        lines.append(line)
    return lines


def sentence_stemmer(text="Who am I?"):
    text = punctuation_remover(text)
    text = stopword_remover(text)
    text = stemmer(text)
    return text
