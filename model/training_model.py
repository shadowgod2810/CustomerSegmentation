import pandas as pd
import pickle
from sklearn.cluster import KMeans

customer_data = pd.read_csv('../data/Mall_Customers.csv')

X = customer_data.iloc[:, [3, 4]].values

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)

kmeans.fit(X)

with open('../model/Segmentation_model.pkl', 'wb') as f:
    pickle.dump(kmeans, f)