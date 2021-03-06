# PATH

csvPath = "C:/Users/sfenton/Code/Repositories/CO2/DATA/210413_PM_CO2_data"
# outputPath = 'C:/Users/sfenton/Code/Repositories/CO2/RESULTS/'

displayParams = {"csvPath": "C:/Users/sfenton/Code/Repositories/CO2/DATA/210413_PM_CO2_data", "outputPath":'C:/Users/sfenton/Code/Repositories/CO2/RESULTS/',
                 'showAccuracy': True, 'showThetas': True, 'showAll' : False, 'showPlot' : True, 'archive': False, 'reference': '211104'}

# DATA

xQualLabels = ['Sector','Type','Basement' ,'Foundations','Ground Floor','Superstructure','Cladding', 'BREEAM Rating'] #]
xQuantLabels = ['GIFA (m2)','Storeys','Typical Span (m)', 'Typ Qk (kN_per_m2)'] # ]

# allvalues = ['Sector_Other', 'Sector_Residential', 'Sector_Cultural', 'Sector_Educational', 'Sector_Mixed Use', 'Sector_Commercial',
#  'Sector_Industrial', 'Type_New Build (Brownfield)', 'Type_New Build (Greenfield)', 'Type_Mixed New Build/Refurb',
#  'Basement_None', 'Basement_Partial Footprint', 'Basement_Full Footprint', 'Foundations_Piled Ground Beams',
#  'Foundations_Mass Pads/Strips', 'Foundations_Raft', 'Foundations_Piles (Pile Caps)', 'Foundations_Reinforced Pads/Strips',
#  'Foundations_', 'Ground Floor_Suspended RC', 'Ground Floor_Ground Bearing RC', 'Ground Floor_Suspended Precast',
#  'Ground Floor_Raft', 'Ground Floor_Other', 'Superstructure_In-Situ RC', 'Superstructure_CLT Frame',
#  'Superstructure_Steel Frame, Precast', 'Superstructure_Masonry, Concrete', 'Superstructure_Steel Frame, Composite',
#  'Superstructure_Steel Frame, Other', 'Superstructure_Masonry, Timber', 'Superstructure_Other', 'Superstructure_Timber Frame',
#  'Superstructure_Steel Frame, Timber', 'Cladding_Masonry + SFS', 'Cladding_Lightweight Only', 'Cladding_Stone + Masonry',
#  'Cladding_Glazed/Curtain Wall', 'Cladding_Masonry Only', 'Cladding_Stone + SFS', 'Cladding_Other', 'Cladding_Lightweight + SFS',
#  'Cladding_Timber + SFS', 'Cladding_Timber Only', 'BREEAM Rating_Unknown', 'BREEAM Rating_Very Good', 'BREEAM Rating_Excellent',
#  'BREEAM Rating_Good', 'BREEAM Rating_Passivhaus', 'BREEAM Rating_Outstanding']

yLabels = ['Calculated tCO2e_per_m2'] #'Calculated Total tCO2e',

scaling = False #True

scalers = {'scaling': False, 'method': 'skl_standardscale','positiveValue': 5, 'qinf': 0.25, 'qsup': 0.75 }#methods : 'standardize', 'robustscale', 'skl_robustscale'

# MODEL

powers = {}#'GIFA (m2)': [1, 0.5], 'Storeys':[1, 2, 3], 0.5 ,, 1/3, 1/4  1/5, 1/6,'Storeys':[1, 2, 3] ,'Typical Span (m)': [1, 2, 3],'Typ Qk (kN_per_m2)': [1, 2, 3] }

modelingParams = {"regularisation": 20, "tolerance": 0.1, "method": "accuracy"} #'mse'; "mae"

mixVariables = [] #[['GIFA (m2)','Storeys']], 'Typ Qk (kN_per_m2)'],,['Sector','Type','Basement','Foundations','Ground Floor','Superstructure','Cladding', 'BREEAM Rating' ]], ['Typical Span (m)'],['GIFA (m2)','Storeys','Typical Span (m)', 'Typ Qk (kN_per_m2)'], ['Sector_Residential','Basement_Partial Footprint']