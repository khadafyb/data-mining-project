from sklearn.datasets import load_svmlight_file
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB as MNB, BernoulliNB as BNB
from sklearn.neighbors import KNeighborsClassifier

folderpath=r"D:\my_data"
folder="C:/Users/hanfs/Desktop/data-mining-project/training_data_file.TF.txt"


feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)


#print(y)

X_new1 = SelectKBest(chi2, k=100).fit_transform(X, y)#returns 100 of the best of feature vectors according to the chi squared test
X_new2 = SelectKBest(mutual_info_classif, k=100).fit_transform(X, y)

clf=MNB()
scores = cross_val_score(clf, feature_vectors, targets, cv=5, scoring='f1_macro')


#(x-axis: K; y-axis:fl_macro)
##I believe the K is the x_new(s) and the f1_macro is the scoring items received from the classifier

i=0
while(i<100):
    #print(X_new1[i])
    i += 1

#x1=X_new1
#x2=X_new2
#y1=scores
#z = X_new1.scores_
#for data in x1[1]:
#    print(data)
#print(x1)
#print(type(x1))
#print(x1, x2, y1)

plt.plot(k=100, X_new1 , label="Line 1")
#plt.Plot(x2,y, label="Line 2")
#plt.xlabel('K')
#plt.ylabel('F1 Macro')
#plt.title('') #title given for the data we are supposed to report
#plt.legend()
plt.show()
##above is what should be repeated for the data_files
