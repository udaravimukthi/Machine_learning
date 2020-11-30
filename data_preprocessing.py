# -*- coding: utf-8 -*-

# Mathematical tools library
import numpy as np

#to plot graph


import matplotlib.pyplot as pt

#to manage datasets

import pandas as pd

mydataset = pd.read_csv('mydata.csv')

X_independent = mydataset.iloc[:,:-1].values

Y_dependent = mydataset.iloc[:,3].values

#from sklearn.preprocessing import Impute
#imputerVariable = Imputer(missing_values = 'NaN',
                      #    strategy = 'mean',
                         # axis = 0)
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

imputer.fit(X_independent[:,1:3])

X_independent[:,1:3] = imputer.transform(X_independent[:,1:3])