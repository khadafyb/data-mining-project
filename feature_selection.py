from sklearn.datasets import load_svmlight_file
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif
import matplotlib.pyplot as plt


feature_vectors, targets = load_svmlight_file("/path/to/train_dataset.txt")
X = feature_vectors
y = targets
X_new1 = SelectKBest(chi2, k=100).fit_transform(X, y)
X_new2 = SelectKBest(mutual_info_classif, k=100).fit_transform(X, y)
#(x-axis: K; y-axis:fl_macro)
##I believe the K is the x_new(s) and the f1_macro is the scoring items received from the classifier
x1=X_new1
x2=X_new2
y=#scoring data

plt.plot(x1,y, label="Line 1")
plt.Plot(x2,y, label="Line 2")
plt.xlabel('K')
plt.ylabel('F1 Macro')
plt.title('') #title given for the data we are supposed to report
plt.legend()
plt.show()
##above is what should be repeated for the data_files
