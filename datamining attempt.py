import os
import _pickle as pickle
####from __future__ import print_function
import numpy as np
####import pandas as pd
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction import DictVectorizer
####from nltk.text import TextCollection  ##-- import for vectorize method
####from sklearn feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


stemmer = SnowballStemmer("english")
vec= DictVectorizer()
##creates sparse matrix of document:term<tfidf> 
def vectorize(file):
    vectorizer = TfidfVectorizer()
    X=vectorizer.fit_transform(file)
    features=vectorizer.get_feature_names()
    doc=0
    feature_index=X[doc,:].nonzero()[1]
    tfidf_score=zip(feature_index,[X[doc,q] for q in feature_index])
    for w,s in[(features[i],s) for (i,s) in tfidf_score]:
         return w,s
         
def vectorizer2(file,inputdoc):
     ##print it but just really weird unsure 
     ##https://www.bogotobogo.com/python/NLTK/tf_idf_with_scikit-learn_NLTK.php
     vectorize=TfidfVectorizer()
     tfs=vectorize.fit_transform(file)
     ##inputdoc.write(str(tfs))
     return tfs
##     features=vectorize.get_feature_names()
##     file_index=[n for n in file]
##     df=pd.DataFrame(tfs.T.todense(),index=features,columns=file_index)
##     print(df)
##     
     
class_definition_file={
            "comp.graphics":0,
            "comp.os.ms-windows.misc":0,
            "comp.sys.ibm.pc.hardware":0,
            "comp.sys.mac.hardware":0,
            "comp.windows.x":0,
            "rec.autos":1,
            "rec.motorcycles":1,
            "rec.sport.baseball":1,
            "rec.sport.hockey":1,
            "sci.crypt":2,
            "sci.electronics":2,
            "sci.med":2,
            "sci.space":2,
            "misc.forsale":3,
            "talk.politics.misc":4,
            "talk.politics.guns":4,
            "talk.politics.mideast":4,
            "talk.religion.mis":5,
            "alt.atheism":5,
            "soc.religion.christian":5
        }
f = open("class_definition_file", "w")
data=str(class_definition_file)
f.write(data[1:len(data)-1])

f.close()


folderpath=r"D:\my_data"
folder="C:/Users/khada/Desktop/data-mining-project/mini_newsgroups"
folder2= "C:/Users/hanfs/Desktop/data-mining-project/mini_newsgroups"

filepaths = [folder+'/'+name for name in os.listdir(folder)]
all_files=[]

feature_definition={}
fdc =0 #feature definition counter for the feature-id


# initializing punctuations string  
punc = '''!()-[]{};:'"\, <>./=?@#|$%^&*_~'''

nltk=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#this whole loop allows us to open each folder within the larger directory, and then to create dictionaries for each
for i in filepaths:
    morepaths = [os.path.join(i, name) for name in os.listdir(i)]

    #we should look to see when i is equal to the above directory to then print it's ID number onto the tidy files
    for path in morepaths:
        with open(path, 'r') as f:
            file = f.readlines()
            ##placing vectorize method to create tfidf's seems best placed here but unsure where to place it
            X,y=vectorize(file)
            #we are now exploring lines within the file
            for line in file:

                words = ""
                #checking each word in the line and we are creating a string that removes the punctuation
                for element in line:
                    if element in punc:
                       words = words + " "
                    else:
                        words = words + element
                word = words.rstrip("\n")
                word = word.rstrip("\t")
                word = word.lower()
                word = word.split(" ")

                #after spliting at spaces we are running both of these loops to remove empty lists within the larger list (which is the line) and the stop words but for some reason it has to be done multiple times
                i=0
                while i<10:
                    for element in word:
                        if element == '':
                            word.remove(element)
                        for a in nltk:
                            if element == a:
                                word.remove(element)
                    i = i+1
                #print(word)
                for element in word:
                    testing=stemmer.stem(element)
                    ##creates a list out of the stemmed string in order to vectorize
##                    testing=[testing]
##                    vectorize(testing)
                    if testing in feature_definition:
                        pass
                    else:
                        feature_definition[testing]=fdc
                        fdc = fdc+1
                
                #now that all blanks within the list are removed we need to stem, then after stemming we then create the bag of words                    
f = open("feature_definition_file", "w")
data=str(feature_definition)

##refernce documetation : https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
##data=str(vec.fit_transform(feature_definition).toarray())
##feature_name=vec.get_feature_names()
##print("feature names: " + str(feature_name))
f.write(data[1:len(data)-1])

f.close()                       

                
                
q="C:/Users/khada/Desktop/data-mining-project/outfile.txt"
print("done")
##q = open("check file_file", "w")
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import load_svmlight_file
clf=MultinomialNB()

##features_vectorst,targets=load_svmlight_file("C:/Users/khada/Desktop/data-mining-project/check file_file.txt")
features_vectorst,targets=load_svmlight_file(X,True,True)
##q.close()
print("done 2")

##https://www.oreilly.com/library/view/applied-text-analysis/9781491963036/ch04.html
#method to compute tf-idf takes all documents and tokenizes, goes through each document and returns {term: tf-idf} for each term in each document
## def vectorize(file):
##     file=[tokenize(doc) for doc in file]
##     texts = TextCollection(file)
##
##     for doc in file:
##         yield {
##             term: texts.tf_idf(term,doc)
##             for term in doc
##         }

##print(vectorize(morepath))
#method to get vectorized documentation for machine learning 
##takes in a string representation to a list of files 
##docfolder should be a string representation to a folder containing files
##https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
# def machinevector(docfolder):
#     text=os.listdir(docfolder)
#     vectorizer = CountVectorizer()
#     vectorizer.fit(text)
#     vector=vectorizer.transform(text)
#     return(vector.toarray())
