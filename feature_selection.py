#Hannibal Santiago
#Khadafy Bilal
#Data mining project 1
from sklearn.datasets import load_svmlight_file
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB as MNB, BernoulliNB as BNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm  import SVC
import matplotlib.pyplot as plt
folderpath=r"D:\my_data"
folder="C:/Users/khada/Desktop/data-mining-project/training_data_file.TF.txt"


feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)


#print(y)

##X_new1 = SelectKBest(chi2, k=100).fit(X, y)#returns 100 of the best of feature vectors according to the chi squared test
##X_new2 = SelectKBest(mutual_info_classif, k=100).fit_transform(X, y)
##
clfm=MNB()
clfb=BNB()
clfk=KNeighborsClassifier()
clfs=SVC()
##scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
vals=[10,25,50,100]

#(x-axis: K; y-axis:fl_macro)
##I believe the K is the x_new(s) and the f1_macro is the scoring items received from the classifier
for K in vals:
    X_new1 = SelectKBest(chi2, k=K).fit_transform(X, y)#returns 100 of the best of feature vectors according to the chi squared test
    X_new2 = SelectKBest(mutual_info_classif, k=K).fit_transform(X, y)

    scoresm1 = cross_val_score(clfm, X_new1, targets, cv=K, scoring='f1_macro')
    scoresb1 = cross_val_score(clfb, X_new1, targets, cv=K, scoring='f1_macro')
    scoresk1 = cross_val_score(clfk, X_new1, targets, cv=K, scoring='f1_macro')
    scoress1 = cross_val_score(clfs, X_new1, targets, cv=K, scoring='f1_macro')
    figure,axis=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm1=np.array(scoresm1)
    scorenumb1=np.array(scoresb1)
    scorenumk1=np.array(scoresk1)
    scorenums1=np.array(scoress1)
    print(scorenumm1)
    print(scorenumb1)
    print(scorenumk1)
    print(scorenums1)
##    print(scorenum.shape)
    axis[0,0].plot(featurenum,scorenumm1)
    axis[0,0].set_title("multinomial")
    
    axis[0,1].plot(featurenum,scorenumb1)
    axis[0,1].set_title("Bernoulli")
    
    axis[1,0].plot(featurenum,scorenumk1)
    axis[1,0].set_title("kneighbors")
    
    axis[1,1].plot(featurenum,scorenums1)
    axis[1,1].set_title("svc")
    plt.savefig('x_new1'+str(K)+'.pdf')

    scoresm2 = cross_val_score(clfm, X_new2, targets, cv=K, scoring='f1_macro')
    scoresb2 = cross_val_score(clfb, X_new2, targets, cv=K, scoring='f1_macro')
    scoresk2 = cross_val_score(clfk, X_new2, targets, cv=K, scoring='f1_macro')
    scoress2 = cross_val_score(clfs, X_new2, targets, cv=K, scoring='f1_macro')
    figure2,axis2=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm2=np.array(scoresm2)
    scorenumb2=np.array(scoresb2)
    scorenumk2=np.array(scoresk2)
    scorenums2=np.array(scoress2)
    print(scorenumm2)
    print(scorenumb2)
    print(scorenumk2)
    print(scorenums2)
##    print(scorenum.shape)
    axis2[0,0].plot(featurenum,scorenumm2)
    axis2[0,0].set_title("multinomial x_new2")
    
    axis2[0,1].plot(featurenum,scorenumb2)
    axis2[0,1].set_title("Bernoulli x_new2")
    
    axis2[1,0].plot(featurenum,scorenumk2)
    axis2[1,0].set_title("kneighbors x_new2")
    
    axis2[1,1].plot(featurenum,scorenums2)
    axis2[1,1].set_title("svc x_new2")
    plt.savefig('x_new2'+str(K)+'.pdf')
    
folder="C:/Users/khada/Desktop/data-mining-project/training_data_file.IDF.txt"


feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)


#print(y)

##X_new1 = SelectKBest(chi2, k=100).fit(X, y)#returns 100 of the best of feature vectors according to the chi squared test
##X_new2 = SelectKBest(mutual_info_classif, k=100).fit_transform(X, y)
##
clfm=MNB()
clfb=BNB()
clfk=KNeighborsClassifier()
clfs=SVC()
##scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
vals=[10,25,50,100]

#(x-axis: K; y-axis:fl_macro)
##I believe the K is the x_new(s) and the f1_macro is the scoring items received from the classifier
for K in vals:
    X_new1 = SelectKBest(chi2, k=K).fit_transform(X, y)#returns 100 of the best of feature vectors according to the chi squared test
    X_new2 = SelectKBest(mutual_info_classif, k=K).fit_transform(X, y)

    scoresm1 = cross_val_score(clfm, X_new1, targets, cv=K, scoring='f1_macro')
    scoresb1 = cross_val_score(clfb, X_new1, targets, cv=K, scoring='f1_macro')
    scoresk1 = cross_val_score(clfk, X_new1, targets, cv=K, scoring='f1_macro')
    scoress1 = cross_val_score(clfs, X_new1, targets, cv=K, scoring='f1_macro')
    figure,axis=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm1=np.array(scoresm1)
    scorenumb1=np.array(scoresb1)
    scorenumk1=np.array(scoresk1)
    scorenums1=np.array(scoress1)
    print(scorenumm1)
    print(scorenumb1)
    print(scorenumk1)
    print(scorenums1)
##    print(scorenum.shape)
    axis[0,0].plot(featurenum,scorenumm1)
    axis[0,0].set_title("multinomial")
    
    axis[0,1].plot(featurenum,scorenumb1)
    axis[0,1].set_title("Bernoulli")
    
    axis[1,0].plot(featurenum,scorenumk1)
    axis[1,0].set_title("kneighbors")
    
    axis[1,1].plot(featurenum,scorenums1)
    axis[1,1].set_title("svc")
    plt.savefig('x_new1'+str(K)+'.pdf')

    scoresm2 = cross_val_score(clfm, X_new2, targets, cv=K, scoring='f1_macro')
    scoresb2 = cross_val_score(clfb, X_new2, targets, cv=K, scoring='f1_macro')
    scoresk2 = cross_val_score(clfk, X_new2, targets, cv=K, scoring='f1_macro')
    scoress2 = cross_val_score(clfs, X_new2, targets, cv=K, scoring='f1_macro')
    figure2,axis2=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm2=np.array(scoresm2)
    scorenumb2=np.array(scoresb2)
    scorenumk2=np.array(scoresk2)
    scorenums2=np.array(scoress2)
    print(scorenumm2)
    print(scorenumb2)
    print(scorenumk2)
    print(scorenums2)
##    print(scorenum.shape)
    axis2[0,0].plot(featurenum,scorenumm2)
    axis2[0,0].set_title("multinomial x_new2")
    
    axis2[0,1].plot(featurenum,scorenumb2)
    axis2[0,1].set_title("Bernoulli x_new2")
    
    axis2[1,0].plot(featurenum,scorenumk2)
    axis2[1,0].set_title("kneighbors x_new2")
    
    axis2[1,1].plot(featurenum,scorenums2)
    axis2[1,1].set_title("svc x_new2")
    plt.savefig('x_new2'+str(K)+'.pdf')

folder="C:/Users/khada/Desktop/data-mining-project/training_data_file.TFIDF.txt"


feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)


#print(y)

##X_new1 = SelectKBest(chi2, k=100).fit(X, y)#returns 100 of the best of feature vectors according to the chi squared test
##X_new2 = SelectKBest(mutual_info_classif, k=100).fit_transform(X, y)
##
clfm=MNB()
clfb=BNB()
clfk=KNeighborsClassifier()
clfs=SVC()
##scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
vals=[10,25,50,100]

#(x-axis: K; y-axis:fl_macro)
##I believe the K is the x_new(s) and the f1_macro is the scoring items received from the classifier
for K in vals:
    X_new1 = SelectKBest(chi2, k=K).fit_transform(X, y)#returns 100 of the best of feature vectors according to the chi squared test
    X_new2 = SelectKBest(mutual_info_classif, k=K).fit_transform(X, y)

    scoresm1 = cross_val_score(clfm, X_new1, targets, cv=K, scoring='f1_macro')
    scoresb1 = cross_val_score(clfb, X_new1, targets, cv=K, scoring='f1_macro')
    scoresk1 = cross_val_score(clfk, X_new1, targets, cv=K, scoring='f1_macro')
    scoress1 = cross_val_score(clfs, X_new1, targets, cv=K, scoring='f1_macro')
    figure,axis=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm1=np.array(scoresm1)
    scorenumb1=np.array(scoresb1)
    scorenumk1=np.array(scoresk1)
    scorenums1=np.array(scoress1)
    print(scorenumm1)
    print(scorenumb1)
    print(scorenumk1)
    print(scorenums1)
##    print(scorenum.shape)
    axis[0,0].plot(featurenum,scorenumm1)
    axis[0,0].set_title("multinomial")
    
    axis[0,1].plot(featurenum,scorenumb1)
    axis[0,1].set_title("Bernoulli")
    
    axis[1,0].plot(featurenum,scorenumk1)
    axis[1,0].set_title("kneighbors")
    
    axis[1,1].plot(featurenum,scorenums1)
    axis[1,1].set_title("svc")
    plt.savefig('x_new1'+str(K)+'.pdf')

    scoresm2 = cross_val_score(clfm, X_new2, targets, cv=K, scoring='f1_macro')
    scoresb2 = cross_val_score(clfb, X_new2, targets, cv=K, scoring='f1_macro')
    scoresk2 = cross_val_score(clfk, X_new2, targets, cv=K, scoring='f1_macro')
    scoress2 = cross_val_score(clfs, X_new2, targets, cv=K, scoring='f1_macro')
    figure2,axis2=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm2=np.array(scoresm2)
    scorenumb2=np.array(scoresb2)
    scorenumk2=np.array(scoresk2)
    scorenums2=np.array(scoress2)
    print(scorenumm2)
    print(scorenumb2)
    print(scorenumk2)
    print(scorenums2)
##    print(scorenum.shape)
    axis2[0,0].plot(featurenum,scorenumm2)
    axis2[0,0].set_title("multinomial x_new2")
    
    axis2[0,1].plot(featurenum,scorenumb2)
    axis2[0,1].set_title("Bernoulli x_new2")
    
    axis2[1,0].plot(featurenum,scorenumk2)
    axis2[1,0].set_title("kneighbors x_new2")
    
    axis2[1,1].plot(featurenum,scorenums2)
    axis2[1,1].set_title("svc x_new2")
    plt.savefig('x_new2'+str(K)+'.pdf')

folder="C:/Users/khada/Desktop/data-mining-project/training_data_file.Boolean.txt"


feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)


#print(y)

##X_new1 = SelectKBest(chi2, k=100).fit(X, y)#returns 100 of the best of feature vectors according to the chi squared test
##X_new2 = SelectKBest(mutual_info_classif, k=100).fit_transform(X, y)
##
clfm=MNB()
clfb=BNB()
clfk=KNeighborsClassifier()
clfs=SVC()
##scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
vals=[10,25,50,100]

#(x-axis: K; y-axis:fl_macro)
##I believe the K is the x_new(s) and the f1_macro is the scoring items received from the classifier
for K in vals:
    X_new1 = SelectKBest(chi2, k=K).fit_transform(X, y)#returns 100 of the best of feature vectors according to the chi squared test
    X_new2 = SelectKBest(mutual_info_classif, k=K).fit_transform(X, y)

    scoresm1 = cross_val_score(clfm, X_new1, targets, cv=K, scoring='f1_macro')
    scoresb1 = cross_val_score(clfb, X_new1, targets, cv=K, scoring='f1_macro')
    scoresk1 = cross_val_score(clfk, X_new1, targets, cv=K, scoring='f1_macro')
    scoress1 = cross_val_score(clfs, X_new1, targets, cv=K, scoring='f1_macro')
    figure,axis=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm1=np.array(scoresm1)
    scorenumb1=np.array(scoresb1)
    scorenumk1=np.array(scoresk1)
    scorenums1=np.array(scoress1)
    print(scorenumm1)
    print(scorenumb1)
    print(scorenumk1)
    print(scorenums1)
##    print(scorenum.shape)
    axis[0,0].plot(featurenum,scorenumm1)
    axis[0,0].set_title("multinomial")
    
    axis[0,1].plot(featurenum,scorenumb1)
    axis[0,1].set_title("Bernoulli")
    
    axis[1,0].plot(featurenum,scorenumk1)
    axis[1,0].set_title("kneighbors")
    
    axis[1,1].plot(featurenum,scorenums1)
    axis[1,1].set_title("svc")
    plt.savefig('x_new1'+str(K)+'.pdf')

    scoresm2 = cross_val_score(clfm, X_new2, targets, cv=K, scoring='f1_macro')
    scoresb2 = cross_val_score(clfb, X_new2, targets, cv=K, scoring='f1_macro')
    scoresk2 = cross_val_score(clfk, X_new2, targets, cv=K, scoring='f1_macro')
    scoress2 = cross_val_score(clfs, X_new2, targets, cv=K, scoring='f1_macro')
    figure2,axis2=plt.subplots(2,2)
    ##f1=X_new1.columns
    f=list(range(0,K))
    featurenum=np.array(f)
    scorenumm2=np.array(scoresm2)
    scorenumb2=np.array(scoresb2)
    scorenumk2=np.array(scoresk2)
    scorenums2=np.array(scoress2)
    print(scorenumm2)
    print(scorenumb2)
    print(scorenumk2)
    print(scorenums2)
##    print(scorenum.shape)
    axis2[0,0].plot(featurenum,scorenumm2)
    axis2[0,0].set_title("multinomial x_new2")
    
    axis2[0,1].plot(featurenum,scorenumb2)
    axis2[0,1].set_title("Bernoulli x_new2")
    
    axis2[1,0].plot(featurenum,scorenumk2)
    axis2[1,0].set_title("kneighbors x_new2")
    
    axis2[1,1].plot(featurenum,scorenums2)
    axis2[1,1].set_title("svc x_new2")
    plt.savefig('x_new2'+str(K)+'.pdf')

 
