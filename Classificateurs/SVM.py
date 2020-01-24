import pandas as pd
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras import utils as np_utils
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

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
    X = plant.iloc[:, 1:]
   
    return X,y 

def load_test_data():
    x, y = load_numeric_training()
    
    x_train, x_test, y_train, y_test = train_test_split(x, y,train_size = 1-0.2, test_size = 0.2, random_state =100)

    return (x_train, y_train), (x_test, y_test)

def main():
    (X_train, y_train),(X_test, y_test)=load_test_data()
    #Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel
    
    #Train the model using the training sets
    clf.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)



    # Model Accuracy: how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred, normalize=True))

    # Model Precision: what percentage of positive tuples are labeled as such?
    print("Precision:",metrics.precision_score(y_test, y_pred, average='micro'))


    # Model Recall: what percentage of positive tuples are labelled as such?
    print("Recall:",metrics.recall_score(y_test, y_pred, average='micro'))


main()
