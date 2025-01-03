import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.cluster import KMeans

dataset = pd.read_csv('iris.csv')
x = dataset.iloc[:,[0,1,2,3]].values

wcss = [] 

for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++',max_iter = 300,n_init = 10,random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

# plotting the results onto a line graph, allowing us to observe 'The elbow'
plt.plot(range(1,11),wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()

# Applying kmeans to the dataset / creating the kmeans classifier
kmeans = KMeans(n_clusters = 3,init = 'k-means++',max_iter = 300,n_init = 10,random_state = 9)
y_kmeans = kmeans.fit_predict(x)

#Visualising the clusters 
plt.scatter(x[y_kmeans == 0,0],x[y_kmeans == 0,1],s = 100,c = 'red',label = 'Iris-sentosa')

plt.scatter(x[y_kmeans == 1,0],x[y_kmeans == 1,1],s = 100,c = 'blue',label = 'Iris-versicolour')

plt.scatter(x[y_kmeans == 2,0],x[y_kmeans == 2,1], s = 100,c = 'green',label = 'Iris-virginica')

# Plotting the entroids of the clusters

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s = 100,c = 'yellow',label = 'Centroids')

plt.legend()
plt.show()
