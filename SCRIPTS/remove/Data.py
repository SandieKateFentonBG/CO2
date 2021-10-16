import numpy as np

def logitize(xQuali, possibleValues):
    output = dict()
    for label, column in xQuali.items():
        for sublabel in possibleValues[label]:
            output['_'.join([label, sublabel])] = [1 if value == possibleValues[label].index(sublabel) else 0 for value in column]
    return output

def countPowers(powers):
    count = 0
    for powerList in powers.values():
        count += len(powerList) - 1  # todo : remove -1 once columns deleted in dataframe
    return count

#TODO : 1. where integrate these cross validation functions?
# do we feed the entire x, y df to the model, and the model splits it, or do we feed only the training to the model?

#self.xTrain, self.yTrain = distributeData(X, Y)[0]

def splitData(X, Y, groupCount = 5):
    cutoffIndex = [int(X.shape[0] * 0.2*i) for i in range(groupCount)]+[X.shape[0]]
    xTrainSets, yTrainSets = [],[] #[]
    for i in range(groupCount):
        xTrainSets.append(X[cutoffIndex[i]:cutoffIndex[i+1]])
        yTrainSets.append(Y[cutoffIndex[i]:cutoffIndex[i+1]])
    return xTrainSets, yTrainSets

def distributeData(X, Y, testGroup = 4):
    xTrainSets, yTrainSets = splitData(X, Y)
    xTest, yTest = xTrainSets.pop(testGroup), yTrainSets.pop(testGroup)
    xTrain, yTrain= np.vstack([xTrainSets[i] for i in range(len(xTrainSets))]), np.vstack([yTrainSets[i] for i in range(len(yTrainSets))])

    return (xTrain, yTrain), (xTest, yTest)

#TODO : 1 - end


class Data:
    def __init__(self, rawData):
        self.x = dict(rawData.xQuanti)
        self.x.update(logitize(rawData.xQuali, rawData.possibleQualities))
        self.y = rawData.y

    def asDataframe(self, powers=None, scale=False):  # Todo: scale fct here
        numValues = len(next(iter(self.x.values())))
        x = np.zeros((numValues, len(self.x)))
        y = np.zeros((numValues, len(self.y)))
        for i in range(numValues):  # 80
            x[i, :] = np.array([self.x[f][i] for f in self.x.keys()]) #todo : remove xquanti column if power
            y[i, :] = np.array([self.y[f][i] for f in self.y.keys()])

        #Todo :  2. MODIF
        if scale: # Todo: scale fct here - is this ok ; should i scale y? if stdv == 0?
            x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)
            #y = (y - np.mean(y, axis=0)) / np.std(y, axis=0)
        #Todo : 2 - end

        if powers:
            x = np.hstack((x, self.powerUpDataframe(powers, numValues)))
        return x, y

    def powerUpDataframe(self, powers, numValues):
        xPowers = np.zeros((numValues, countPowers(powers)))
        colIndex = 0
        for label, powerList in powers.items():
            for power in powerList:
                if power != 1:   # todo : remove line once columns deleted in dataframe
                    xPowers[:, colIndex] = np.power(self.x[label], power)
                    colIndex += 1
        return xPowers



