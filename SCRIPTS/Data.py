def logitize(xQuali, possibleValues):
    output = dict()
    for label, column in xQuali.items():
        for sublabel in possibleValues[label]:
            output['_'.join([label, sublabel])] = [1 if value == possibleValues[label].index(sublabel) else 0 for value in column]
    return output


class Data:
    def __init__(self, rawData):
        self.x = dict(rawData.xQuanti)
        self.x.update(logitize(rawData.xQuali, rawData.possibleValues))
        self.y = rawData.y

    def asDataframe(self):  # Todo: scale fct here
        import numpy as np
        numValues = len(next(iter(self.x.values())))
        x = np.zeros((numValues, len(self.x)))
        y = np.zeros((numValues, len(self.y)))
        for i in range(numValues):  # 80
            x[i, :] = np.array([self.x[f][i] for f in self.x.keys()])
            y[i, :] = np.array([self.y[f][i] for f in self.y.keys()])
        return x, y
