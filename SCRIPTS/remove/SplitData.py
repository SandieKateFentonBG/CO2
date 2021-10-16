import numpy as np

#TODO : 2. where integrate these cross validation functions?
# do we feed the entire x, y df to the model, and the model splits it, or do we feed only the training to the model?


def splitData(X, Y, groupCount = 5):
    cutoffIndex = [int(X.shape[0] * 0.2*i) for i in range(groupCount)]+[X.shape[0]]
    xTrainSets, yTrainSets = [],[] #[]
    for i in range(groupCount):
        xTrainSets.append(X[cutoffIndex[i]:cutoffIndex[i+1]])
        yTrainSets.append(Y[cutoffIndex[i]:cutoffIndex[i+1]])
    return xTrainSets, yTrainSets

def distributeData(X, Y, testGroup, absolute = 1): #TODO : 3. specify the y you are working with
    xTrainSets, yTrainSets = splitData(X, Y)
    xTest, yTest = xTrainSets.pop(testGroup), yTrainSets.pop(testGroup)
    xTrain, yTrain= np.vstack([xTrainSets[i] for i in range(len(xTrainSets))]), np.vstack([yTrainSets[i] for i in range(len(yTrainSets))])

    #return (xTrain, yTrain), (xTest, yTest)
    return (xTrain, yTrain[:,absolute]), (xTest, yTest[:, absolute])

#TODO : 1 - end
