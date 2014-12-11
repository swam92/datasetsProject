from sklearn.cluster import KMeans

#lets call it predictors!!THIS IS WHERE WE WILL DEFINE AN ARRAY OF VALUES TO cluster
kmeans = KMeans()
kmeans.fit(predictors)