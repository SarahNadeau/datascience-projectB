#Baseline for linear regression model:
#This is the mean of the dependent variable.
mean_of_prices = prices.mean()

#SSE = squared error = sum of (actual - predicted) squared
SSE = sklearn.metrics.mean_squared_error(y_true = test_target, y_pred = predictions)
#SST = squared error for baseline = sum of (actual - baseline prediction) squared
SST = sklearn.metrics.mean_squared_error(y_true = test_target, y_pred = mean of prices)
#R squared = 1 - (SSE/SST)
R_squared = 1 - (SSE/SST)
print(R_squared)
#If R_squared is close to 1, then the linear regression model is good. (SSE is a lot less that SST)

#Baseline for KNN:
#This should be the value that is most common in the dependent variable.

housing_data[ 'After1970' ] = housing_data['YearBuilt'] > 1970
After1970 = housing_data.filter('After1970')
housing_data[ 'Before1970'] = housing_data['YearBuilt'] < 1970
Before1970 = housing_data.filter('Before1970')

if After1970.count()> Before1970.count():
    baseline_prediction = After1970
else:
    baseline_prediction = Before1970

    
#baseline_prediction is the value of the unknown value that is expected. Finding how many of the actual values 
#correspond to the baseline_prediction. The more the number of values that match, the better the model. 
#want True positive rate to be as high as possible - high sensitivity. Senistivity = True positive/
#(True positive + False negative) 
for i in range(len(housing_data_year):
               result = 0
               result1
               #I wrote is in to state that the test_target is inside the DataFrame of baseline_prediction.
               #Is this the wrong way to do it?
               #Just wondering, Predicted column is a binary column with value 0 or 1 or True or False. 
               #Where is this column?
               if test_target in baseline_prediction:
                           result.append(1)
               else:
                           result1.append(1)
total = result+result1
               
Therefore, Sensitivity = result/(total)
    Accuracy.           
               
QUESTIONS: 
               
##Should we create an ROC curve to test our classifier is good? 
               
##If accuracy needs to be mentioned, KNeighborsClassifier has accuracy_score(y_test, prediction).
               
##I think the assignment asks us to show if the colums we chose have a linear rel. with the dependent variable.
# Should I make residual graphs for them?

#KNN basically shows the relationship between the features selected and the YearBuilt, right? 
#For KNN features, OverallCond, ExterCond, ExterQual, SaleCondition - newer building, better condition (usually)
    #BldgType, HouseStyle, RoofStyle, GarageType - similar buildings are built in similar time periods.
    # Should we use YrRemodAdd since YrRemodAdd stays the same if the buildign wasn't remodelled? 
    #I couldn't understand what relationship I could draw between GarageCars and YrBuilt. 
               #Could someone please explain it?
               
# To show that these features are good for the KNN model, we could show that we are using classified data
               #using bar graphs maybe? I don't know if this is necessary although it seems like they want us to 
               #show this for the lin. reg. model.