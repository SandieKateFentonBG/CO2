import numpy as np


def logitize(xQuali, possibleValues):
    output = dict()
    for label, column in xQuali.items():
        for sublabel in possibleValues[label]:
            output['_'.join([label, sublabel])] = [1 if value == possibleValues[label].index(sublabel) else 0 for value in column]
    return output

def scale(xQuanti):
    xQuantiScaled = dict()
    for label, column in xQuanti.items():
        xQuantiScaled[label] = list((column - np.mean(column)) / np.std(column))
    return xQuantiScaled


def countPowers(powers):
    count = 0
    for powerList in powers.values():
        count += len(powerList)
    return count

def powerCross(): #todo
    #mix features x1x2 etc
    pass

def convert(): #todo
    #elevate to logarithm/inverse proportionalty/other relations
    pass


class Data:
    def __init__(self, rawData, scaling):
        if scaling:  # todo - should this be here
            self.x = scale(rawData.xQuanti)  # todo
        else:
            self.x = dict(rawData.xQuanti)
        self.x.update(logitize(rawData.xQuali, rawData.possibleQualities))
        self.y = rawData.y

    def asDataframes(self, powers=None, mixVariables=None, batchCount=5):
        x, y = self.asDataframe(powers, mixVariables)
        cutoffIndex = batchCount if x.shape[0] % batchCount == 0\
            else [int(x.shape[0] / batchCount * i) for i in range(1, batchCount)]
        return np.split(x, cutoffIndex), np.split(y, cutoffIndex)

    def asDataframe(self, powers={}, mixVariables=[]):
        numValues = len(next(iter(self.x.values())))
        x = np.zeros((numValues, len(self.x)-len(powers)))
        y = np.zeros((numValues, len(self.y)))
        for i in range(numValues):  # 80
            x[i, :] = np.array([self.x[f][i] for f in self.x.keys() if f not in powers.keys()])
            y[i, :] = np.array([self.y[f][i] for f in self.y.keys()])
        if powers:
            x = np.hstack((x, self.powerUpDataframe(powers, numValues)))
        if mixVariables:
            x = np.hstack((x, self.crossVariablesDataframe(mixVariables, numValues)))
        return x, y

    def powerUpDataframe(self, powers, numValues):
        xPowers = np.zeros((numValues, countPowers(powers)))
        colIndex = 0
        for label, powerList in powers.items():
            for power in powerList:
                xPowers[:, colIndex] = np.power(self.x[label], power)
                colIndex += 1
        return xPowers

    def crossVariablesDataframe(self,mixVariables, numValues):
        xCross = np.zeros((numValues, len(mixVariables))) #80, 2
        colIndex = 0
        for list in mixVariables: #todo :this works for qtt only! - should remove the qtt/qlt that you only want in mix/powers
            arrays = [np.array([self.x[f] for f in list]).T]
            # print(type(arrays), len(arrays))
            # print(type(arrays[0]), len(arrays[0]))
            # print(arrays[0].shape)
            xCross[:, colIndex] = np.prod(np.hstack(arrays), axis=1)
            # for i in range(numValues):
            #     print(arrays[0][i], xCross[:, colIndex][i])

            colIndex += 1
        return xCross



