from RawData import RawData
from Data import Data
from Data import *
from ModelAssessment import rotation
from Dashboard import *
import Search
import Plot

# import Plot


"""
------------------------------------------------------------------------------------------------------------------------
1.DATA
------------------------------------------------------------------------------------------------------------------------
"""
rdat = RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels)
dat = Data(rdat, scalers)
x, y, variabLabels = dat.asDataframe(powers, mixVariables)
xSets, ySetsMultiVar, xlabels = dat.asDataframes(powers, mixVariables)

"""
------------------------------------------------------------------------------------------------------------------------
2. SEARCH
------------------------------------------------------------------------------------------------------------------------
"""
# Single scenario
# ----------------------------------------------------------------------------------------------------------------------

# results = Search.scenarioResults(yLabels, xSets, ySetsMultiVar, variabLabels, modelingParams, displayParams)
# print("before", len(xSets[0]), len(xSets[0][0]), xSets[0][0])

# Parameter study
# ----------------------------------------------------------------------------------------------------------------------

param = 'regularisation'
paramList = [0, 0.001, 0.01, 0.1, 1, 5, 20, 100, 1000]
paramStudy = Search.paramResults(paramList, yLabels, xSets, ySetsMultiVar, variabLabels, modelingParams, param) #,displayParams

# label = "Calculated tCO2e_per_m2" #Calculated Total tCO2e
# xList = paramList
# yList = [paramStudy[k]["Quality(%s)" % label]["Mean quality (%s)" % modelingParams['method']]for k,v in paramStudy.items() if type(v)==dict]
# Plot.plotGraph(xList, yList, param, "Quality(%s)" % label, displayParams, title=None, figure_size=(8, 12), plot=True)

# Power study
# ----------------------------------------------------------------------------------------------------------------------

variable = 'GIFA (m2)'
powerList = [[1], [1, 2], [1, 2, 3]] #, [1, 2, 3, 4, 5], [1, 0.5], [1, 0.5, (1/3)],[1, 0.5, (1/3), 0.25, 0.2], [1, 0.5, (1/3), 0.25, 0.2]]
print("before", len(xSets[0]), len(xSets[0][0]), xSets[0][0])
powerstudy = Search.powerResults(dat, modelingParams, powers, mixVariables, variable, powerList, yLabels, displayParams)
label = "Calculated tCO2e_per_m2" #Calculated Total tCO2e
xList = powerList
yList = [powerstudy[k]["Quality(%s)" % label]["Mean quality (%s)" % modelingParams['method']]for k,v in powerstudy.items() if type(v)==dict]
print(xList, yList)
Plot.plotGraph(xList, yList, param, "Quality(%s)" % label, displayParams, title=None, figure_size=(8, 12), plot=True)

#todo: make plots with values not numbered

# Mix study
# ----------------------------------------------------------------------------------------------------------------------
# mixedVariables = xQualLabels + xQuantLabels
# variabMixList = [[['GIFA (m2)','Storeys'], ['GIFA (m2)','Typ Qk (kN_per_m2)']],[['GIFA (m2)', 'Typ Qk (kN_per_m2)','Storeys']]] #[], 'Typ Qk (kN_per_m2)']
# mixStudy = Search.mixResults(dat, modelingParams, powers, mixedVariables, variabMixList, yLabels, displayParams)

# Global study
# ----------------------------------------------------------------------------------------------------------------------


"""
------------------------------------------------------------------------------------------------------------------------
3. ADVISE
------------------------------------------------------------------------------------------------------------------------
"""