from LinearRegression import LinReg
import numpy as np


def rotation(xSets, ySets, modelingParams):
    thetas, evals = [], []
    for i in range(len(xSets)):
        xTrain = np.vstack([batch for batch in xSets if batch is not xSets[i]])
        yTrain = np.concatenate([batch for batch in ySets if batch is not ySets[i]])
        theta, eval = learn(xTrain, yTrain, xSets[i], ySets[i], modelingParams)
        thetas.append(theta), evals.append(eval)
    return sum(evals) / len(evals), thetas, evals


def learn(xTrain, yTrain, xTest, yTest, modelingParams):
    model = LinReg(regul=modelingParams["regularisation"])
    model.calibration(xTrain, yTrain)
    return model.theta, model.evaluation(xTest, yTest, modelingParams["method"], modelingParams["tolerance"])
