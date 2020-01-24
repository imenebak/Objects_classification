import os
import re
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from keras import utils as np_utils
import matplotlib.pyplot as plt
def load_numeric_training():
    plant = pd.read_csv('Train1.txt', skiprows=0)
    plant.head()
    y = plant.pop('Class')
    # Since the labels are textual, so we encode them categorically
    encoder = LabelEncoder()
    encoder.fit(y)
    # convert integers to dummy variables
    encoded_Y = encoder.transform(y)
    # standardize the data by setting the mean to 0 and std to 1
    y = np_utils.to_categorical(encoded_Y)
    X = plant.iloc[:, 1:]
   
    return X,y 
from sklearn import tree
def load_test_data():
    x, y = load_numeric_training()
    x_train, x_test, y_train, y_test = train_test_split(x, y,train_size = 1-0.2, test_size = 0.2, random_state =42)
    return (x_train, y_train), (x_test, y_test)


def Knn_():
    (X_train, y_train),(X_test, y_test)=load_test_data()
    error_rate = []
    #Build a knn classifior

    neighbors = np.arange(1, 5) 
    train_accuracy = np.empty(len(neighbors)) 
    test_accuracy = np.empty(len(neighbors)) 
      
    # Loop over K values 
    for i, k in enumerate(neighbors): 
        knn = KNeighborsClassifier(n_neighbors=k) 
        knn.fit(X_train, y_train) 
          
        # Compute traning and test data accuracy 
        train_accuracy[i] = knn.score(X_train, y_train) 
        test_accuracy[i] = knn.score(X_test, y_test) 
      
    # Generate plot 
    plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy') 
    plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy') 
      
    plt.legend() 
    plt.xlabel('n_neighbors') 
    plt.ylabel('Accuracy') 
    plt.show()

    

def main():   
    Knn_()
    #Decesion_tree()
main()
