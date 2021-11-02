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

dat = Data(rdat, scalers) #this has to be rebuilt in study power

x, y, variabLabels = dat.asDataframe(powers, mixVariables)

xSets, ySetsMultiVar, xlabels = dat.asDataframes(powers, mixVariables)

# results = Search.scenarioResults(yLabels, xSets, ySetsMultiVar, variabLabels, modelingParams, displayParams)


"""
------------------------------------------------------------------------------------------------------------------------
1.RUN
------------------------------------------------------------------------------------------------------------------------
# """
# # #
param = 'regularisation'
paramList = [0, 0.001, 0.01, 0.1, 1, 5, 20, 100, 1000]
variable = 'GIFA (m2)'
powerList = [[1], [1, 2], [1, 2, 3]] #, [1, 2, 3, 4, 5], [1, 0.5], [1, 0.5, (1/3)],[1, 0.5, (1/3), 0.25, 0.2], [1, 0.5, (1/3), 0.25, 0.2]]
# #
# paramStudy = Search.studyParam(paramList, yLabels, xSets, ySetsMultiVar, variabLabels, modelingParams, param, displayParams)
# # #
# # # x_list, y_list = paramList, paramStudy['accuracy(Calculated Total tCO2e)']
# # # Plot.plot_sns_graph(x_list, y_list, param, 'accuracy(Calculated Total tCO2e)', title=None, figure_size=(8,12), folder=None, plot=False)
# #
# # powerstudy, fullStudy = Display.studyPower('GIFA (m2)', powerList, powers, mixVariables, dat, yLabels, modelingParams, displayParams)
# # print(powerstudy)
#
powerstudy = Search.powerResults(dat, modelingParams, powers, mixVariables, variable, powerList, yLabels, displayParams)