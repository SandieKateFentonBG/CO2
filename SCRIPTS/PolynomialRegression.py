import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from RawData import RawData
from Data import *
from Dashboard import *

rdat = RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels)
dat = Data(rdat, scalers)
X, y, variabLabels = dat.asDataframe(powers, mixVariables)
xSets, ySetsMultiVar, xlabels = dat.asDataframes(powers, mixVariables)

"""
A. Scaling :
Normalization :  
- scaling technique in which values are shifted and rescaled so that they end up ranging between 0 and 1.
- It is also known as Min-Max scaling. 
- Good to use when you know that the distribution of your data does not follow a Gaussian distribution

Standardization : 
- scaling technique where the values are centered around the mean with a unit standard deviation. 
- This means that the mean of the attribute becomes zero and the resultant distribution has a unit standard deviation. 
- Helpful in cases where the data follows a Gaussian distribution. 

Should I Normalize? what to do with the one-hot encoded values - these should not be scaled?

B. Split train/test :
Where is this done?

"""
# print(len(X), X)

from sklearn.linear_model import LinearRegression

def TrainTestSplit(xSets, ySets, testSetIndex=1):

    xTrain = np.vstack([batch for batch in xSets if batch is not xSets[testSetIndex]])
    yTrain = np.concatenate([batch for batch in ySets if batch is not ySets[testSetIndex]])
    return (xTrain, yTrain), (xSets[testSetIndex], ySets[testSetIndex])
testSetIndex = 4
(xTrain, yTrain), (xTest, yTest) = TrainTestSplit(xSets, ySetsMultiVar, testSetIndex)
print(len(xTrain),len(yTrain),len(xTest),len(yTest))

print('test', testSetIndex)

"""
1
"""
lin_reg = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)
lin_reg.fit(xTrain, yTrain, sample_weight=None)
lin_reg.predict(xTest)
s = lin_reg.score(xTest, yTest, sample_weight=None)
p = lin_reg.get_params()
c = lin_reg.coef_
i = lin_reg.intercept_
print('1')
print('score',s)
print('param', p)
#print('coef', len(c[0]), c)
print('intercept', i)

"""
2
"""
lin_reg2 = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)
pa = lin_reg2.get_params()
pa['normalize'] = True
lin_reg2.set_params(**pa)
lin_reg2.fit(xTrain, yTrain, sample_weight=None)
lin_reg2.predict(xTest)

sc = lin_reg2.score(xTest, yTest, sample_weight=None)
co = lin_reg2.coef_
inter = lin_reg2.intercept_
print('2')
print('score',sc)
print('param', pa)
# print('coef', len(co[0]), co)
print('intercept', inter)

"""
3
"""
lin_reg3 = LinearRegression(fit_intercept=False, normalize=True, copy_X=True, n_jobs=None)
par = lin_reg3.get_params()
lin_reg3.fit(xTrain, yTrain, sample_weight=None)
lin_reg3.predict(xTest)

sco = lin_reg3.score(xTest, yTest, sample_weight=None)
coe = lin_reg3.coef_
interc = lin_reg3.intercept_
print('3')
print('score',sco)
print('param', par)
# print('coef', len(coe[0]), coe)
print('intercept', interc)