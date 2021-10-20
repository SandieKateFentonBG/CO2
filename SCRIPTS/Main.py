from RawData import RawData
from Data import Data
from Data import *
from ModelAssessment import rotation
from Dashboard import *

rd = RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels)
dat = Data(rd, scaling)
# print(type(dat.crossVariablesDataframe(mixVariables, 80)), (dat.crossVariablesDataframe(mixVariables, 80).shape))

#print(len(dat.x), dat.x)

#print(dat.asDataframe(mixVariables=mixVariables)[0].shape, dat.asDataframe(mixVariables=mixVariables)[0])
# print(dat.asDataframe(powers, mixVariables)[0].shape, dat.asDataframe(powers, mixVariables)[0])
x, y, xlabels = dat.asDataframe(powers, mixVariables)
print("here", xlabels)
#xSets, ySetsMultiVar = dat.asDataframes(powers, mixVariables)


def checkyLabels(yLabels, xSets, modelingParams, ySetsMultiVar):
    for i in range(len(yLabels)):
        print("------> " + yLabels[i])
        ySets = [batch[:, i] for batch in ySetsMultiVar]
        score, theta, scores = rotation(xSets, ySets, modelingParams)
        print("Mean quality (%s) :" % modelingParams['method'], score)
        print("Batchs quality (%s) :" % modelingParams['method'], scores)
        print("First Theta (%s) :" % len(theta[0]))
        print(len(theta[0]), type(theta[0]), theta[0])
        # for t in theta:
        #     print(t)
        print()

        print("theta - mean", np.array([np.mean(theta, axis =0)]))
        print("theta - std ", np.array([np.std(theta, axis=0)]))





# checkyLabels(yLabels, xSets, modelingParams, ySetsMultiVar)