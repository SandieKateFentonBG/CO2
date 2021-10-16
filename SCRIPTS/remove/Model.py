import numpy as np


def splitData(self, X, Y, testSet = 0):
    if shuffle:
        pass  # TODO
    cutoffIndex = [int(X.shape[0] * 0.2)*i for i in range(5)]
    xTrainSets = [X[cutoffIndex[j]:cutoffIndex[j+1], :]for j in cutoffIndex]+[X[cutoffIndex[-1]:,:]]
    yTrainSets = [y[cutoffIndex[j]:cutoffIndex[j+1], :]for j in cutoffIndex]+[y[cutoffIndex[-1]:,:]]
    xTestSets, yTestSets = xTrainSets.pop(testSet), yTrainSets.pop(testSet)
    return (xTrainSets, yTrainSets), (xTestSets, yTestSets)


class Model:
    def __init__(self, powers, theta=None, regul=0):
        self.powers = powers
        if theta is None:
            pass
        self.theta = theta
        self.regul = regul





    def prediction(self, X):

        pass

    def calibration(self):
        pass

    def instantiate_theta(self):

