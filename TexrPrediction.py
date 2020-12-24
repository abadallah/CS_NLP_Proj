import nltk
import operator
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.corpus import reuters
from nltk import bigrams, trigrams, ngrams
from collections import Counter, defaultdict
from nltk.collocations import *
from nltk.corpus import brown


def readData():
  
    #fileName = 'dataset3.txt'
    #file = open(fileName, "r")
    #data = file.read()
    #file.close()


    data = brown.words(categories='news')
    return data


def Norm(data):
   # tokens = word_tokenize(data)

    tokens = [word.lower() for word in data if word.isalpha()]
    return tokens


def Create_biGrem(data):
    return nltk.collocations.BigramCollocationFinder.from_words(data)


def Ex_gram(_data, num):
    data = " ".join(_data)
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [" ".join(grams) for grams in n_grams]


def Count_unit(data):
    fd = nltk.FreqDist(data)
    print(fd.values())


def Calculate_Pro(Biograme, unigrameCount, lastWard, v):
    GarmPro = {}
    for BioIn in set(Biograme):
        if lastWard == BioIn.split()[0]:
            GarmPro[BioIn] = (Counter(Biograme)[BioIn] + 1) / (unigrameCount + v)
            print(BioIn.split()[1],GarmPro[BioIn])
    return (max(GarmPro.items(), key=operator.itemgetter(1))[0].split()[1] if len(GarmPro)!=0 else 0)


if __name__ == '__main__':
    #read Dataset File
    data = readData()

    # Normlize the data
    NormliseData = Norm(data)

    #Enter the Input
    MYinput = input().lower()

    lastWard = MYinput.split()[-1] if len(MYinput) != 0 else ""




    #create Bigram
    Biograme = Ex_gram(NormliseData, 2)

    #the count of unirgram of last input ward
    unigrameCount = Counter(Ex_gram(NormliseData, 1))[lastWard]

    #unique words in dataset for smothing
    Vocablary = set(NormliseData)


    #Calulate proparty and select Max Pro
    result =  Calculate_Pro(Biograme, unigrameCount,lastWard,len(Vocablary))

    print(result)
