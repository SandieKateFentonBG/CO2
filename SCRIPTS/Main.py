from RawData import RawData
from Data import *
from Dashboard import *
import Search
import Plot

"""
------------------------------------------------------------------------------------------------------------------------
1.DATA
------------------------------------------------------------------------------------------------------------------------
"""
rdat = RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels)
dat = Data(rdat, scalers)
x, y, variabLabels = dat.asDataframe(powers, mixVariables)
xSets, ySetsMultiVar, xlabels = dat.asDataframes(powers, mixVariables)

# for yLabel in yLabels:
#     for xLabel in xQualLabels + xQuantLabels:
#         rdat.visualize(displayParams, yLabel=yLabel, xLabel=xLabel)
# dat.dataModification(powers, mixVariables)

"""
------------------------------------------------------------------------------------------------------------------------
2. SEARCH
------------------------------------------------------------------------------------------------------------------------
"""
unit = "Calculated tCO2e_per_m2" #Calculated Total tCO2e
#todo : currently pictures saved overrite previous ones !

# Single scenario
# ----------------------------------------------------------------------------------------------------------------------
#
# results = Search.scenarioResults(yLabels, xSets, ySetsMultiVar, variabLabels, modelingParams, displayParams)

# Parameter study
# ----------------------------------------------------------------------------------------------------------------------
#
# param = 'regularisation'
# paramList = [0, 0.001, 0.01, 0.1, 1, 5, 10, 15, 20, 25, 50, 100, 1000]
#
# def runParamStudy(param, paramList):
#     paramStudy = Search.paramResults(paramList, yLabels, xSets, ySetsMultiVar, variabLabels, modelingParams, param, displayParams) #
#     xLabel, yLabel = param,  "%s" % modelingParams['method'] + " (%s)" % unit
#     xList, yList = paramList, [paramStudy[k]["Quality(%s)" % unit]["Mean quality (%s)" % modelingParams['method']]for k,v in paramStudy.items() if type(v)==dict]
#     Plot.plotGraph(xList, yList, xLabel, yLabel, displayParams, folder=param)
#     return xList, yList
#
#
# print(param, runParamStudy(param, paramList))

# Power study
# ----------------------------------------------------------------------------------------------------------------------

variable = 'Storeys' #'GIFA (m2)'
powerList = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 0.5], [1, 0.5, (1 / 3)], [1, 0.5, (1 / 3), 0.25],
             [1, 0.5, (1 / 3), 0.25, 0.2]]

def runPowerStudy(variable, powerList):
    xLabel, yLabel = variable + ' Polynomial Exponents', "%s" % modelingParams['method'] + " (%s)" % unit
    powerstudy = Search.powerResults(dat, modelingParams, powers, mixVariables, variable, powerList, yLabels, displayParams)
    xList, yList = powerList, [powerstudy[k]["Quality(%s)" % unit]["Mean quality (%s)" % modelingParams['method']]for k,v in powerstudy.items() if type(v)==dict]
    Plot.plotGraph(xList, yList, xLabel, yLabel, displayParams, convertxList=True, folder = xLabel)
    return xList, yList


print(variable, runPowerStudy(variable, powerList))

# Mix study
# ----------------------------------------------------------------------------------------------------------------------

# variabMixList = [[['GIFA (m2)']+[elem]] for elem in xQuantLabels if elem!='GIFA (m2)'] #! has to be of dim [[[]]] #todo: make this work for xQualLabels
# mixedVariables = xQuantLabels + xQualLabels #list(set([label[i] for label in variabMixList[j] for i in range(len(label))])) #todo: change this
#
# def runMixStudy(mixedVariables, variabMixList):
#     mixStudy = Search.mixResults(dat, modelingParams, powers, mixedVariables, variabMixList, yLabels, displayParams)
#     xLabel, yLabel= 'Combined Variables', "%s" % modelingParams['method'] + " (%s)" % unit
#     xList, yList = variabMixList, [mixStudy[k]["Quality(%s)" % unit]["Mean quality (%s)" % modelingParams['method']]for k,v in mixStudy.items() if type(v)==dict]
#     Plot.plotGraph(xList, yList, xLabel, yLabel, displayParams, convertxList=True, folder = xLabel)
#     return xList, yList
#
#
# print('Mix', runMixStudy(mixedVariables, variabMixList))

# Global study
# ----------------------------------------------------------------------------------------------------------------------


"""
------------------------------------------------------------------------------------------------------------------------
3. ADVISE
------------------------------------------------------------------------------------------------------------------------
"""