import numpy as np



def logitize(xQuali, possibleValues):
    output = dict()
    for label, column in xQuali.items():
        for sublabel in possibleValues[label]:
            output['_'.join([label, sublabel])] = [1 if value == possibleValues[label].index(sublabel) else 0 for value in column]
    return output

def xscale(xQuanti):
    xQuantiScaled = dict()
    for label, column in xQuanti.items():
        xQuantiScaled[label] = list((column - np.mean(column)) / np.std(column))
    return xQuantiScaled

#def scale(xQuanti, method = 'skl_robustscale', positiveValue = 10, qinf= 0.25, qsup= 0.75): #'standardize', 'robustscale', 'skl_robustscale'
def scale(xQuanti, method, positiveValue, qinf, qsup): #'standardize', 'robustscale', 'skl_robustscale'
    xQuantiScaled = dict()
    # todo : fix positive value issue for powers < 1
    for label, column in xQuanti.items():
        if method == 'standardize':
            xQuantiScaled[label] = list((column - np.mean(column)) / np.std(column))
            if positiveValue:
                xQuantiScaled[label] = [x + positiveValue for x in xQuantiScaled[label]]#todo : check this is fine - allows to ensure positive values
        elif method == 'robustscale':
            xQuantiScaled[label] = list((column - np.median(column)) /(np.quantile(column, qinf)-np.quantile(column, qsup)))
            if positiveValue:
                xQuantiScaled[label] = [x + positiveValue for x in xQuantiScaled[label]]
        elif method == 'skl_robustscale':#use sklearn robustscaler
            from sklearn.preprocessing import RobustScaler
            for label, column in xQuanti.items():
                array = np.array(column).reshape(-1, 1)
                rs = RobustScaler(quantile_range=(qinf, qsup)).fit(array)
                xQuantiScaled[label] = list(rs.transform(array)[0])#todo : not working, flatten output - Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
        elif method == 'skl_standardscale':#use sklearn standardscaler
            from sklearn.preprocessing import StandardScaler
            for label, column in xQuanti.items():
                array = np.array(column).reshape(-1, 1)
                rs = StandardScaler().fit(array)
                xQuantiScaled[label] = list(rs.transform(array))


    return xQuantiScaled




def countPowers(powers):
    count = 0
    for powerList in powers.values():
        count += len(powerList)
    return count


def convert(): #todo
    #elevate to logarithm/inverse proportionalty/other relations
    pass


class Data:
    def __init__(self, rawData, scalers):
        if scalers['scaling']:  # todo - should this be here
            self.x = scale(rawData.xQuanti, scalers['method'],scalers['positiveValue'],scalers['qinf'],scalers['qsup'])
        else:
            self.x = dict(rawData.xQuanti)
        self.x.update(logitize(rawData.xQuali, rawData.possibleQualities))
        self.y = rawData.y

    def asDataframes(self, powers=None, mixVariables=None, batchCount=5):
        x, y, xlabels = self.asDataframe(powers, mixVariables)
        cutoffIndex = batchCount if x.shape[0] % batchCount == 0\
            else [int(x.shape[0] / batchCount * i) for i in range(1, batchCount)]
        return np.split(x, cutoffIndex), np.split(y, cutoffIndex), xlabels

    def asDataframe(self, powers={}, mixVariables=[]): #todo : this should maybe build a df with everything then remove all cilumns thatarent in mix/powers...
        numValues = len(next(iter(self.x.values())))
        x = np.zeros((numValues, len(self.x)-len(powers)))
        y = np.zeros((numValues, len(self.y)))
        xlabels = [f for f in self.x.keys() if f not in powers.keys()]
        for i in range(numValues):  # 80
            x[i, :] = np.array([self.x[f][i] for f in self.x.keys() if f not in powers.keys()])
            y[i, :] = np.array([self.y[f][i] for f in self.y.keys()])
        if powers:
            xPowers, xPowerLabels = self.powerUpVariables(powers, numValues)
            x = np.hstack((x, xPowers))
            xlabels += xPowerLabels
        if mixVariables:
            xCross, xCrossLabels = self.combineVariables(mixVariables, numValues)
            x = np.hstack((x,xCross))
            xlabels += xCrossLabels
        return x, y, xlabels


    def powerUpVariables(self, powers, numValues):
        xPowers = np.zeros((numValues, countPowers(powers)))
        colIndex = 0
        xPowerLabels = []
        for label, powerList in powers.items():
            for power in powerList:
                xPowers[:, colIndex] = np.float_power(np.abs(self.x[label]), power)  # todo: check fix : np.abs
                xPowerLabels.append(label + '_exp' + str(power))
                colIndex += 1
        return xPowers, xPowerLabels

    def combineVariables(self, mixVariables, numValues):
        #todo : this doesn't work if the keys aren't in the linear labels:
        # ex : y =  GIFA  + STOREY + GIFA * STOREY ok
        # but y = GIFA * Storey ko
        xCross = np.zeros((numValues, len(mixVariables))) #80, 2
        colIndex = 0
        xCrossLabels = []
        for list in mixVariables:
            arrays = [np.array([self.x[f] for f in list]).T]
            xCrossLabels.append('*'.join(list))
            xCross[:, colIndex] = np.prod(np.hstack(arrays), axis=1)
            colIndex += 1
        return xCross, xCrossLabels

    def dataModification(self, powers={}, mixVariables=[]):

        numValues = len(next(iter(self.x.values())))
        xUnchanged = np.zeros((numValues, len(self.x)))
        yUnchanged = np.zeros((numValues, len(self.y)))
        xlabelsUnchanged = [f for f in self.x.keys()]
        for i in range(numValues):  # 80
            xUnchanged[i, :] = np.array([self.x[f][i] for f in self.x.keys()])
            yUnchanged[i, :] = np.array([self.y[f][i] for f in self.y.keys()])

        print('Unchanged Labels: ', xlabelsUnchanged)
        print('xUnchanged : ', type(xUnchanged), xUnchanged.shape)
        print(xUnchanged[0])
        print('yUnchanged : ', type(yUnchanged), yUnchanged.shape, )
        print(yUnchanged[0])
        print('')

        xNew, yNew, xlabelsNew = self.asDataframe(powers, mixVariables)

        print('New Labels: ', xlabelsNew)
        print('xNew : ', type(xNew), xNew.shape)
        print(xNew[0])
        print('yNew : ', type(yNew), yNew.shape)
        print(yNew[0])
        print('')

