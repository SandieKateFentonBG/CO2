from RawData import RawData
from Data import Data
from ModelAssessment import rotation


csvPath = "C:/Users/sfenton/Code/Repositories/CO2/DATA/210413_PM_CO2_data"
outputPath = 'C:/Users/sfenton/Code/Repositories/CO2/RESULTS/'

xQualLabels = ['Sector', 'Type', 'Basement', 'Foundations', 'Ground Floor', 'Superstructure', 'Cladding', 'BREEAM Rating']
xQuantLabels = ['GIFA (m2)', 'Storeys', 'Typical Span (m)', 'Typ Qk (kN_per_m2)']
yLabels = ['Calculated Total tCO2e', 'Calculated tCO2e_per_m2']

powers = {'GIFA (m2)': [1, 2, 3], 'Storeys': [1, 2], 'Typical Span (m)': [1, 2], 'Typ Qk (kN_per_m2)': [1, 2, 3]}

dat = Data(RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels))
xSets, ySetsMultiVar = dat.asDataframes(powers, False)
for i in range(len(yLabels)):
    print("------> " + yLabels[i])
    ySets = [batch[:, i] for batch in ySetsMultiVar]
    print(rotation(xSets, ySets))
