from sklearn.datasets import load_svmlight_file as svmlight
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB as MNB, BernoulliNB as BNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

folderpath=r"D:\my_data"
folder="C:/Users/hanfs/Desktop/data-mining-project/training_data_file.TF.txt"


#wondering if we should just hard code each path file but most likely because there is only 3
feature_vectors, targets = svmlight(folder)


###Lets Generate the Classifier items###
clf=MNB()
scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))




clf=BNB()
scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

##Notes to understand the function
#


#####
clf= KNeighborsClassifier()
scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

##
#



#####
clf = SVC()
scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
##Notes to understand the function
#

###Use Classifier

###Now make the rest of the files data but this does now work


