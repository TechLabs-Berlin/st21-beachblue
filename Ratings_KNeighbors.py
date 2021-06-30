import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import mean_squared_error as MSE

from sklearn.model_selection import train_test_split

knn = KNeighborsClassifier(n_neighbors = 4)

df = pd.read_csv('playas_with_parcial_ratings.csv')

mapping = {'Yes': 1, 'No': 0,'Parcial': 0.5, np.nan: 0}

quality = {'Excellent': 1, 'Good':0.8, 'Sufficient':0.4, 'Poor':0.2, 'Not classified':0}

pop = {'High': 1, 'Medium': 0.8, 'Low': 0.4, 'Vey low': 0.2, 'Null': 0}

#print(df['quality2019'].unique())

df['Sea_Promenade_1'] = (df['Sea_Promenade'].replace(mapping))*3

df['Nudism_1'] = (df['Nudism'].replace(mapping))*4

df['Blue_Flag_1'] = (df['Blue_Flag'].replace(mapping))*4

df['Reachable_by_bus_1'] = (df['Reachable_by_bus'].replace(mapping))*3

df['Parking_1'] = (df['Parking'].replace(mapping))*3

df['Toilets_1'] = (df['Toilets'].replace(mapping))*5

df['Footbaths_1'] = (df['Footbaths'].replace(mapping))*4

df['Showers_1'] = (df['Showers'].replace(mapping))*5

df['Public_Telephones_1'] = (df['Public_Telephones'].replace(mapping))*2

df['Trashcans_1'] = (df['Trashcans'].replace(mapping))*2

df['Child_Zone_1'] = (df['Child_Zone'].replace(mapping))*4

df['Sport_Zone_1'] = (df['Sport_Zone'].replace(mapping))*4

df['Yacht_Club_1'] = (df['Yacht_Club'].replace(mapping))*4

df['Surfing_Zone_1'] = (df['Surfing_Zone'].replace(mapping))*4

df['quality2019_1'] = (df['quality2019']).replace(quality)*5

df['Popularity_1'] = (df['Popularity']).replace(pop)*5

df['Sum'] = df[['Sea_Promenade_1','Nudism_1','Blue_Flag_1','Reachable_by_bus_1','Parking_1','Toilets_1','Footbaths_1','Public_Telephones_1','Trashcans_1','Child_Zone_1','Sport_Zone_1','Yacht_Club_1','Surfing_Zone_1','quality2019_1', 'Popularity_1']].sum(axis=1)

print(df['Sum'].describe())

ranges = [0,10,20,30,40,np.inf]

cat = ['1','2','3','4','5']

#df['ratings_1'] = pd.qcut(df['Sum'], q = 5, labels = cat)

df['ratings_2'] = pd.cut(df['Sum'], bins = ranges, labels = cat)

print(df['ratings_2'].unique())

print(df[['ratings_2','Sum','rating']].head())

df = df[~df['ratings_2'].isna()]

new = df[df['ratings_2'].isna()]

#print(new.head())

#print(df.describe())

#df.to_csv('playas_new_ratings.csv')

data = df[['Sea_Promenade_1','Nudism_1','Blue_Flag_1','Reachable_by_bus_1','Parking_1','Toilets_1','Footbaths_1','Public_Telephones_1','Trashcans_1','Child_Zone_1','Sport_Zone_1','Yacht_Club_1','Surfing_Zone_1','Popularity_1','quality2019_1']]

print(data.shape)

print(df['ratings_2'].shape)

X = data

y = df['ratings_2']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.4, random_state=100)

#print(X_train.describe())

#print(y_train.describe())

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print(y_pred)

print(knn.score(X_test, y_test))

mse_dt = MSE(y_pred, y_test)

rmse_dt = (mse_dt)**0.5

# Print rmse_dt
print("Test set RMSE of dt: {:.2f}".format(rmse_dt))

counts, bins, patches = plt.hist(y_test, bins = 9)

plt.title('Actual Values')

plt.show()
counts_1, bins_1, patches_1 = plt.hist(y_test, bins = 9)

plt.title('Predicted Values')

plt.show()
# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)

train_accuracy = np.empty(len(neighbors))

test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train,y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')

plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')

plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')

plt.legend()

plt.xlabel('Number of Neighbors')

plt.ylabel('Accuracy')

plt.show()

#print(df['Sum'].describe())"""

""" print(df['Sum'].head())

print(df['Sum'].max())

print(df['Sum'].mean())

print(df['Sum'].min()) """

"""print(df['Sum'].unique())

print(df['Sea_Promenade_1'].unique())

print(df['Nudism_1'].unique())

print(df['Blue_Flag_1'].unique())

print(df['Reachable_by_bus_1'].unique())

print(df['Parking_1'].unique())

print(df['Toilets_1'].unique())

print(df['Footbaths_1'].unique())

print(df['Public_Telephones_1'].unique())

print(df['Trashcans_1'].unique())

print(df['Child_Zone_1'].unique())

print(df['Sport_Zone_1'].unique())

print(df['Yacht_Club_1'].unique())

print(df['Surfing_Zone_1'].unique())"""

""" print(df['Sea_Promenade_1'].head())

print(df['Nudism_1'].head())

print(df['Blue_Flag_1'].head())

print(df['Reachable_by_bus_1'].head())

print(df['Parking_1'].head())

print(df['Toilets_1'].head())

print(df['Footbaths_1'].head())

print(df['Public_Telephones_1'].head())

print(df['Trashcans_1'].head())

print(df['Child_Zone_1'].head())

print(df['Sport_Zone_1'].head())

print(df['Yacht_Club_1'].head())

print(df['Surfing_Zone_1'].head(10)) """ 