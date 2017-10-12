import seaborn as sns
import numpy as np
import sklearn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

housing_data = pd.DataFrame.from_csv('cleaned.csv')

# Calculate the baseline for linear regression

# Identify the relevant features
#housing_features = housing_data[:, []]

#determine strength of correlation for features of interest
X = pd.DataFrame(housing_data,columns=['OverallQual', 'GarageCars', 'GarageArea', 'YearRemodAdd', 'YearBuilt', 'WoodDeckSF', 'OpenPorchSF', 'LotArea', 'SalePrice']) 
corr = np.corrcoef(X,rowvar=False) #rowvar = False b/c columns are features

print(len(corr))
print(corr[8])
print(corr)

# Create and test model for linear regression for 5 different train_test splits

# Calculate the baseline for KNN model

# Identify the relevant features

# Create and test KNN model for 5 different train_test splits