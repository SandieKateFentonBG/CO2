import RawData
import Data_Sf
import Model_sf
import ModelInvestigator

import numpy as np

csvPath = "C:/Users/sfenton/Code/Repositories/CO2/DATA/210413_PM_CO2_data"
outputPath = 'C:/Users/sfenton/Code/Repositories/CO2/RESULTS/',

xQualLabels = ['Sector', 'Type', 'Basement', 'Foundations', 'Ground Floor', 'Superstructure', 'Cladding', 'BREEAM Rating']
xQuantLabels = ['GIFA (m2)', 'Storeys', 'Typical Span (m)', 'Typ Qk (kN_per_m2)']
yLabels = ['Calculated Total tCO2e', 'Calculated tCO2e_per_m2']

powers = {'GIFA (m2)': [1, 2, 3], 'Storeys': [1, 2], 'Typical Span (m)': [1, 2], 'Typ Qk (kN_per_m2)': [1, 2, 3]}
#powers = {'GIFA (m2)': [1], 'Storeys': [1], 'Typical Span (m)': [1], 'Typ Qk (kN_per_m2)': [1]}


rd = RawData.RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels)


x, y = Data_Sf.Data(rd).asDataframes(powers, False)

# co2Model = Model_sf.Model(powers, x, y, theta=None, regul=1, testGroup = 0)
# thetaOpt = co2Model.calibration() #todo: how can there ne a single pinv solution?
# eval = co2Model.evaluation() #todo: what does this number represent? how can i know if it is a good result?
#
# print(rd.possibleQualities)
# print(thetaOpt)
# ModelInvestigator.assessTheta(thetaOpt, rd.possibleQualities, powers)
#
# l = ModelInvestigator.thetaLabels(rd.possibleQualities, powers)
#
# v = ModelInvestigator.thetaValues(thetaOpt, rd.possibleQualities, powers)
# av = ModelInvestigator.thetaAbsMean(v)
# print(l)
# print(v)
# print(av)






