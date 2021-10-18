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
        count += len(powerList)
    return count

def powerCross(): #todo
    #mix features x1x2 etc
    pass

def convert(): #todo
    #elevate to logarithm/inverse proportionalty/other relations
    pass


class Data:
    def __init__(self, rawData):
        self.x = dict(rawData.xQuanti)
        self.x.update(logitize(rawData.xQuali, rawData.possibleQualities))
        self.y = rawData.y

    def asDataframes(self, scale, powers=None, batchCount=5):
        x, y = self.asDataframe(scale, powers)
        cutoffIndex = batchCount if x.shape[0] % batchCount == 0\
            else [int(x.shape[0] / batchCount * i) for i in range(1, batchCount)]
        return np.split(x, cutoffIndex), np.split(y, cutoffIndex)

    def asDataframe(self, scale, powers={}):
        numValues = len(next(iter(self.x.values())))
        x = np.zeros((numValues, len(self.x)-len(powers)))
        y = np.zeros((numValues, len(self.y)))
        for i in range(numValues):  # 80
            x[i, :] = np.array([self.x[f][i] for f in self.x.keys() if f not in powers.keys()])
            y[i, :] = np.array([self.y[f][i] for f in self.y.keys()])
        if scale:  # Todo: move this into constructor - act only on quantitative variables?
            x = (x - np.mean(x, axis=0)) / np.std(x, axis=0)  # todo : check axis
        if powers:
            x = np.hstack((x, self.powerUpDataframe(powers, numValues)))
        return x, y

    def powerUpDataframe(self, powers, numValues):
        xPowers = np.zeros((numValues, countPowers(powers)))
        colIndex = 0
        for label, powerList in powers.items():
            for power in powerList:
                xPowers[:, colIndex] = np.power(self.x[label], power)
                colIndex += 1
        return xPowers
