#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:49:11 2020

@author: xander999
"""

# Random Forest Classification

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_excel('Revised_School_Rating.xlsx')
dataset=dataset.drop(columns=['Unnamed: 0'])
X = dataset.iloc[:, 1:18]
#y1 contains prediction for Class 10 review
y1 = dataset.iloc[:, 18]
#y2 contains prediction for Class 12 review
y2=dataset.iloc[:,19]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y1, test_size = 0.25, random_state = 0)


#Handling Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lb=LabelEncoder()
ohe=OneHotEncoder(categorical_features=[1,2,3,5,6])
X_train.iloc[:,1]=lb.fit_transform(X_train.iloc[:,1])
X_train.iloc[:,2]=lb.fit_transform(X_train.iloc[:,2])
X_train.iloc[:,3]=lb.fit_transform(X_train.iloc[:,3])
X_train.iloc[:,5]=lb.fit_transform(X_train.iloc[:,5])
X_train.iloc[:,6]=lb.fit_transform(X_train.iloc[:,6])

X_train=ohe.fit_transform(X_train).toarray()

X_train=X_train[:,3:127]

X_test.iloc[:,1]=lb.fit_transform(X_test.iloc[:,1])
X_test.iloc[:,2]=lb.fit_transform(X_test.iloc[:,2])
X_test.iloc[:,3]=lb.fit_transform(X_test.iloc[:,3])
X_test.iloc[:,5]=lb.fit_transform(X_test.iloc[:,5])
X_test.iloc[:,6]=lb.fit_transform(X_test.iloc[:,6])

X_test=ohe.fit_transform(X_test).toarray()


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)