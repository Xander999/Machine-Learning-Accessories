#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:33:50 2019

@author: xander999
"""

import numpy as np
import pandas as pd
import random as r

df1 = pd.read_excel('School_Dataset.xlsx')
# processing range of data.....from columns 10-18
for j in range(10,19):
    a=df1.iloc[:,j]
    for i in range(len(df1)):
        if(not pd.isnull(a[i])):
            x=[int(c) for c in a[i].split('-')]
            a[i]=sum(x)/2
    df1.iloc[:,j].replace(np.NaN,df1.iloc[:,j].mean(), inplace=True)
    #print(df1.iloc[:10,j])
#Replacing missing values wih mean


#droppings certain unwanted coloumns
df2=df1.drop(columns=['Name of your School','Address of the School','Sports', 'Available Subjects'])


#Handling class 10(4th coloumn) and (16th coloumn) marks
l=[4,16]
for i in l:
    a=df2.iloc[:,i]
    for j in range(len(a)):
        if(not pd.isnull(a[j])):
            if(int(a[j])<1):
                a[j]=float(a[j])*100
            elif(int(a[j])<10):
                a[j]=float(a[j])*10
    df2.iloc[:,i].replace(np.NaN,df2.iloc[:,i].mean(), inplace=True)


df2.to_excel('INITIAL_Revised_School_Rating.xlsx')


#Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
lb=LabelEncoder()
df2.iloc[:,1]=lb.fit_transform(df2.iloc[:,1])
df2.iloc[:,2]=lb.fit_transform(df2.iloc[:,2])
df2.iloc[:,3]=lb.fit_transform(df2.iloc[:,3])
df2.iloc[:,5]=lb.fit_transform(df2.iloc[:,5])
df2.iloc[:,6]=lb.fit_transform(df2.iloc[:,6])
ohe=OneHotEncoder(categorical_features=[0])
df2=ohe.fit_transform(df2).toarray()


#Repeating data via random basis..........Data Replication
df2=pd.read_excel('INITIAL_Revised_School_Rating.xlsx')

df4=df2[:99]
for i in range(0,len(df4)):
    num=r.randrange(2,6,2)
    x=pd.concat([df2[i:i+1]]*num)
    df4=df4.append(x,ignore_index=True)
 
#Shuffling of Data
from sklearn.utils import shuffle
df7=shuffle(df4).reset_index(drop=True)

nn=len(df7)
for i in range(0,nn-1):
    if df7.iloc[i,:].equals(df7.iloc[i+1,:]):
        print(df7[i:i+1])
        x=pd.concat([df7[i+1:i+2]])
        df7=df7.drop(df7.index[i])
        df7=df7.append(x,ignore_index=True)

df7.to_excel('Revised_School_Rating.xlsx')