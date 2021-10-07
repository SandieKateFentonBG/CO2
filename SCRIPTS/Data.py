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

class Data:
    def __init__(self, rawData):
        self.x = dict(rawData.xQuanti)
        self.x.update(logitize(rawData.xQuali, rawData.possibleValues))
        self.y = rawData.y

    def asDataframe(self, powers=None):  # Todo: scale fct here
        numValues = len(next(iter(self.x.values())))
        x = np.zeros((numValues, len(self.x)))
        y = np.zeros((numValues, len(self.y)))
        for i in range(numValues):  # 80
            x[i, :] = np.array([self.x[f][i] for f in self.x.keys()]) #todo : remove xquanti column if power
            y[i, :] = np.array([self.y[f][i] for f in self.y.keys()])
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



