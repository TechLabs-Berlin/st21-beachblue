import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import mean_squared_error as MSE

from sklearn.model_selection import train_test_split

knn = KNeighborsClassifier(n_neighbors = 4)

df = pd.read_csv('playas-with-full-google-ratings.csv')

#mapping the features values in the rangle 0-1

mapping = {'Yes': 1, 'No': 0,'Partial': 0.5, np.nan: 0}

quality = {'Excellent': 1, 'Good':0.8, 'Sufficient':0.4, 'Poor':0.2, 'Not classified':0}

pop = {'High': 1, 'Medium': 0.8, 'Low': 0.4, 'Vey low': 0.2, 'Null': 0}

# Assigning weights to individual features and storing them in new coulmns
 
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


#summing up weights of individual features

df['Sum'] = df[['Sea_Promenade_1','Nudism_1','Blue_Flag_1','Reachable_by_bus_1','Parking_1','Toilets_1','Footbaths_1','Public_Telephones_1','Trashcans_1','Child_Zone_1','Sport_Zone_1','Yacht_Club_1','Surfing_Zone_1','quality2019_1', 'Popularity_1']].sum(axis=1)

#Assigning the sum to rating ranging from 1-5. Example a sum of 40, is assigned between a range 30-40 and then the value is assigned to a rating of 4

ranges = [0,10,20,30,40,np.inf]

cat = ['1','2','3','4','5']

df['ratings_2'] = pd.cut(df['Sum'], bins = ranges, labels = cat)

#if there are NaN values present in ratings those columns are dropped

df = df[~df['ratings_2'].isna()]

new = df[df['ratings_2'].isna()]

#df.to_csv('playas_new_with_all_ratings.csv')

# X and y variables are defined

data = df[['Sea_Promenade_1','Nudism_1','Blue_Flag_1','Reachable_by_bus_1','Parking_1','Toilets_1','Footbaths_1','Public_Telephones_1','Trashcans_1','Child_Zone_1','Sport_Zone_1','Yacht_Club_1','Surfing_Zone_1','Popularity_1','quality2019_1']]

X = data

y = df['ratings_2']

# the dataset is divided in train and test with testing dataset of 40%

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.4, random_state=100)

#fitting the knn model on the train dataset

knn.fit(X_train, y_train)

#predicting the y values with test dataset

y_pred = knn.predict(X_test)

score = knn.score(X_test, y_test)

print("Prediction score of test set: {:.2f}".format(score))

# To find the mean square error of the predicted data

mse_dt = MSE(y_pred, y_test)

rmse_dt = (mse_dt)**0.5

# Print rmse_dt
print("Test set RMSE of dt: {:.2f}".format(rmse_dt))

# plotting the actual data and predicted data

plt.subplot(2,1,1)

counts, bins, patches = plt.hist(y_test)

plt.title('Actual Values')

plt.subplot(2,1,2)

counts_1, bins_1, patches_1 = plt.hist(y_test)

plt.title('Predicted Values')

plt.tight_layout()

plt.show()

# To find out the best KNN value for the features chosen to fit in KNN model

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