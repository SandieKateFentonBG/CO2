# PATH

csvPath = "C:/Users/sfenton/Code/Repositories/CO2/DATA/210413_PM_CO2_data"
outputPath = 'C:/Users/sfenton/Code/Repositories/CO2/RESULTS/'

# DATA

xQualLabels = ['Sector','Type','Basement','Foundations','Ground Floor','Superstructure','Cladding', 'BREEAM Rating' ] # ]
xQuantLabels = ['GIFA (m2)','Storeys' , 'Typical Span (m)', 'Typ Qk (kN_per_m2)'] #]
yLabels = ['Calculated Total tCO2e', 'Calculated tCO2e_per_m2']

scaling = False #True

# MODEL

powers = {'GIFA (m2)': [1, 2, 3],'Storeys': [1, 2, 3],'Typical Span (m)': [1, 2, 3],'Typ Qk (kN_per_m2)': [1, 2, 3]} # }

modelingParams = {"regularisation": 1, "tolerance": 0.20, "method": "accuracy"} #'mse'; "mae"