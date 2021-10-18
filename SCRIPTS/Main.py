from RawData import RawData
from Data import Data
from ModelAssessment import rotation
from Dashboard import *


dat = Data(RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels))
xSets, ySetsMultiVar = dat.asDataframes(scaling, powers)

for i in range(len(yLabels)):
    print("------> " + yLabels[i])
    ySets = [batch[:, i] for batch in ySetsMultiVar]
    score, theta, scores = rotation(xSets, ySets, modelingParams)
    print("Mean quality (%s) :" % modelingParams['method'], score)
    print("Batchs quality (%s) :" % modelingParams['method'], scores)
    print("First Theta : ")
    for t in theta:
        print(t)
    print()

