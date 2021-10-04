import RawData
import Data

csvPath = "C:/Users/sfenton/Code/Repositories/CO2/DATA/210413_PM_CO2_data"
outputPath = 'C:/Users/sfenton/Code/Repositories/CO2/RESULTS/',

xQualLabels = ['Sector', 'Type', 'Basement', 'Foundations', 'Ground Floor', 'Superstructure', 'Cladding', 'BREEAM Rating']
xQuantLabels = ['GIFA (m2)', 'Storeys', 'Typical Span (m)', 'Typ Qk (kN_per_m2)']
yLabels = ['Calculated Total tCO2e', 'Calculated tCO2e_per_m2']



rd = RawData.RawData(csvPath, ';', 5, xQualLabels, xQuantLabels, yLabels)
x, y = Data.Data(rd).asDataframe()
print(type(x))
print((x.shape))
print(x)