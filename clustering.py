#Hannibal Santiago
#Khdafy Bilal
#Data Mining Project 1


from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.datasets import load_svmlight_file
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, mutual_info_classif
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB as MNB, BernoulliNB as BNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np 

folder="C:/Users/hanfs/Desktop/data-mining-project/training_data_file.TF.txt"

feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)
classification_labels = y
n_clusters=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
returning=[]
for n in n_clusters:
    kmeans_model = KMeans(n).fit(feature_vectors)
    print(kmeans_model)
    clustering_labels = kmeans_model.labels_
    SC=metrics.silhouette_score(feature_vectors, clustering_labels, metric='euclidean')
    NMI=metrics.normalized_mutual_info_score(classification_labels, clustering_labels)
    data=(n, SC, NMI)
    returning.append(data)
#single_linkage_model = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(feature_vectors) confused if mylast element needs to be in the information as well
#print(single_linkage_model)
print(returning)

x=np.array(returning[0])
y1=np.array(returning[1])
y2=np.array(returning[2])

plt.title("Clusting: SC & NMI")
plt.xlabel("n's")
plt.ylabel("Measurements")
plt.plot(x,y1, label="SC")
plt.plot(x,y2, label="NMI")
plt.show()



folder="C:/Users/hanfs/Desktop/data-mining-project/training_data_file.IDF.txt"

feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)
classification_labels = y
n_clusters=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
returning=[]
for n in n_clusters:
    kmeans_model = KMeans(n_clusters=n).fit(feature_vectors)
    clustering_labels = kmeans_model.labels_
    SC=metrics.silhouette_score(feature_vectors, clustering_labels, metric='euclidean')
    NMI=metrics.normalized_mutual_info_score(classification_labels, clustering_labels)
    data=(n, SC, NMI)
    returning.append(data)
#single_linkage_model = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(feature_vectors) confused if mylast element needs to be in the information as well
#print(single_linkage_model)
print(returning)

x=np.array(returning[0])
y1=np.array(returning[1])
y2=np.array(returning[2])

plt.title("Clusting: SC & NMI")
plt.xlabel("n's")
plt.ylabel("Measurements")
plt.plot(x,y1, label="SC")
plt.plot(x,y2, label="NMI")
plt.show()

folder="C:/Users/hanfs/Desktop/data-mining-project/training_data_file.TFIDF.txt"

feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)
classification_labels = y
n_clusters=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
returning=[]
for n in n_clusters:
    kmeans_model = KMeans(n_clusters=n).fit(feature_vectors)
    clustering_labels = kmeans_model.labels_
    SC=metrics.silhouette_score(feature_vectors, clustering_labels, metric='euclidean')
    NMI=metrics.normalized_mutual_info_score(classification_labels, clustering_labels)
    data=(n, SC, NMI)
    returning.append(data)
#single_linkage_model = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(feature_vectors) confused if mylast element needs to be in the information as well
#print(single_linkage_model)
print(returning)

x=np.array(returning[0])
y1=np.array(returning[1])
y2=np.array(returning[2])

plt.title("Clusting: SC & NMI")
plt.xlabel("n's")
plt.ylabel("Measurements")
plt.plot(x,y1, label="SC")
plt.plot(x,y2, label="NMI")
plt.show()

folder="C:/Users/hanfs/Desktop/data-mining-project/training_data_file.Boolean.txt"

feature_vectors, targets = load_svmlight_file(folder)
X = feature_vectors
X = X.astype(int)
y = targets
y = y.astype(int)
classification_labels = y
n_clusters=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
returning=[]
for n in n_clusters:
    kmeans_model = KMeans(n_clusters=n).fit(feature_vectors)
    clustering_labels = kmeans_model.labels_
    SC=metrics.silhouette_score(feature_vectors, clustering_labels, metric='euclidean')
    NMI=metrics.normalized_mutual_info_score(classification_labels, clustering_labels)
    data=(n, SC, NMI)
    returning.append(data)
#single_linkage_model = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(feature_vectors) confused if mylast element needs to be in the information as well
#print(single_linkage_model)
print(returning)

x=np.array(returning[0])
y1=np.array(returning[1])
y2=np.array(returning[2])

plt.title("Clusting: SC & NMI")
plt.xlabel("n's")
plt.ylabel("Measurements")
plt.plot(x,y1, label="SC")
plt.plot(x,y2, label="NMI")
plt.show()
