from ModelAssessment import rotation
import Data
import numpy as np

# class Search: #todo : should this become a class?
#     def __init__(self, data, modelingParams, powers, mixVariables):
#         self.data = data
#         self.modelingParams = modelingParams
#         self.powers = powers
#         self.mixVariables = mixVariables
#         x, y, variabLabels = data.asDataframe(powers, mixVariables)
#         self.variabLabels = variabLabels
#         xSets, ySetsMultiVar, xlabels = data.asDataframes(powers, mixVariables)
#         self.xSets = xSets
#         self.ySetsMultiVar = ySetsMultiVar
#
#
def scenarioDataframe(data, powers, mixVariables):

    return data.asDataframes(powers, mixVariables) #xSets, ySetsMultiVar, variabLabels

def scenarioResults(yLabels, xSets, ySetsMultiVar, variabLabels, modelingParams, displayParams = None):

    """
    Computes results for 1 single scenario including all ylabels

    :param yLabels: unit studied
    :param variabLabels: variables in the hypothesis function
    :param xSets: sets used for cross validation
    :param modelingParams: model parameters
    :param ySetsMultiVar: target sets including all studied units
    :return:
    """


    Results = {"Modelling Parameters": modelingParams}
    for i in range(len(yLabels)):
        ySets = [batch[:, i] for batch in ySetsMultiVar]
        score, theta, scores = rotation(xSets, ySets, modelingParams)
        Results["Quality(%s)" % yLabels[i]]={"Mean quality (%s)" % modelingParams['method']:score,
                               "Batchs quality (%s)" % modelingParams['method']:scores}
        Results["Theta(%s)" % yLabels[i]] ={"Theta - labels": variabLabels,"Theta - first(%s)" % len(theta[0]): theta[0],
                              "Theta - mean": np.array([np.mean(theta, axis =0)]),
                              "Theta - std ": np.array([np.std(theta, axis=0)]),
                              "Theta (%s)" % [len(theta), len(theta[0])]: theta}

    if displayParams:
        scenarioDisplay(Results, yLabels, modelingParams, displayParams)

        if displayParams["archive"]:
            saveStudy(displayParams, Results)

    return Results

def scenarioDisplay(Results, yLabels, modelingParams, displayParams):

    """
    Displays results for 1 single scenario including all ylabels

    :param yLabels: unit studied
    :param modelingParams: model parameters
    :param displayParams: display parameters
    :return: Displays results of 1 scenario
    """

    for i in range(len(yLabels)):
        if displayParams["showAccuracy"]:
            print("Evaluation(%s) -" % yLabels[i], "Mean quality (%s) :" % modelingParams['method'], Results["Quality(%s)" % yLabels[i]] ["Mean quality (%s)" % modelingParams['method']])
        if displayParams["showThetas"]:
            for k in range(len(Results["Theta(%s)" % yLabels[i]]["Theta - labels"])):
                print(Results["Theta(%s)" % yLabels[i]]["Theta - labels"][k],
                  Results["Theta(%s)" % yLabels[i]]["Theta - mean"][:,k])
            print()
    if displayParams["showAll"]:
        for ks, vs in Results.items():
            print(ks, ':')
            for k, v in vs.items():
                print(k,":", v)
            print()

def paramResults(paramList, yLabels, xSets, ySetsMultiVar, variabLabels, dbModelingParams, modelingParamsKey, displayParams =  None):#todo : change here

    """
    Computes results for multiple values of a selected parameter
    Order - for 1 unit - iterate through all parameter values - then repeat

    :param paramList:
    :param yLabels:
    :param variabLabels:
    :param xSets:
    :param dbModelingParams:
    :param ySetsMultiVar:
    :param displayParams:
    :param modelingParamsKey:
    :return:
    """

    paramStudy = {"studied parameter": modelingParamsKey, "parameter values": paramList}
    keys = []
    base = "<" + '//'.join(variabLabels) + ">"
    for elem in paramList:
        dbModelingParams[modelingParamsKey] = elem
        k = modelingParamsKey + "(%s)  " % elem + "<" + '//'.join(variabLabels) + ">"
        # paramStudy[modelingParamsKey + "(%s)" % elem] = scenarioResults(yLabels, xSets, ySetsMultiVar, variabLabels, dbModelingParams)#todo : change here
        paramStudy[k] = scenarioResults(yLabels, xSets, ySetsMultiVar, variabLabels, dbModelingParams)#todo : change here
        keys.append(k)

    if displayParams:
        # paramDisplay(paramStudy, yLabels, paramList, dbModelingParams, modelingParamsKey, displayParams)
        studyDisplay(modelingParamsKey, paramList, paramStudy, keys, yLabels, dbModelingParams, displayParams,
                      variableText="studied parameter :", listText="parameter values :")

        if displayParams["archive"]:
            saveStudy(displayParams, paramStudy)

    return paramStudy

def paramDisplay(paramStudy, yLabels, paramList, dbModelingParams, modelingParamsKey, displayParams):

    if displayParams['showAll']:
        for k, v in paramStudy.items():
            print(k,":", v)
    if displayParams['showAccuracy']:
        print("studied parameter :", modelingParamsKey)
        print("metric:", "Mean quality (%s)" % dbModelingParams['method'])
        for elem in paramList:
            for label in yLabels:
                print(modelingParamsKey,":", elem, "(%s)" % label,  paramStudy[modelingParamsKey + "(%s)" % elem]["Quality(%s)" % label]["Mean quality (%s)" % dbModelingParams['method']])

def powerResults(data, dbModelingParams, dbPowers, dbMixVariables, variable, variabPowerList, yLabels, displayParams = None): #variabLabels,xSets,ySetsMultiVar,

    """
    Computes results for multiple power combinations of a selected variable
    Order - for 1 unit - iterate through all parameter values - then repeat

    :param variable:
    :param variabPowerList:
    :param dbPowers:
    :param mixVariables:
    :param data:
    :param yLabels:
    :param modelingParams:
    :param displayParams:
    :return:
    """

    variabPowerStudy = {"studied variable": variable, "power values": variabPowerList}

    keys = []
    for p in variabPowerList:

        dbPowers[variable] = p #is a list < might not work
        xSets, ySetsMultiVar, variabLabels = scenarioDataframe(data, dbPowers, dbMixVariables)
        k = "<" + '//'.join(variabLabels) + ">"
        variabPowerStudy[k]= scenarioResults(yLabels, xSets, ySetsMultiVar,variabLabels, dbModelingParams)
        # variabPowerStudy[variable + "_power_" + "(%s)" % p]= scenarioResults(yLabels, xSets, ySetsMultiVar,variabLabels, dbModelingParams)
        keys.append(k)

    if displayParams:
        # powerDisplay(variable, variabPowerList, variabPowerStudy, yLabels, dbModelingParams, displayParams)
        studyDisplay(variable, variabPowerList, variabPowerStudy, keys, yLabels, dbModelingParams, displayParams,
                      variableText="studied variable :", listText="power values :")

        if displayParams["archive"]:
            saveStudy(displayParams, variabPowerStudy, keys, yLabels, dbModelingParams)

    return variabPowerStudy

def powerDisplay(variable, variabPowerList, variabPowerStudy, yLabels, dbModelingParams, displayParams):

    if displayParams['showAll']:
        for k, v in variabPowerStudy.items():
            print(k, ":", v)
    if displayParams['showAccuracy']:
        print("studied variable :", variable)
        print("power values :", variabPowerList)
        print("metric:", "Mean quality (%s)" % dbModelingParams['method'])
        for p in variabPowerList:
            for label in yLabels:
                print(variable + "_power_" + "(%s)" % p,
                      variabPowerStudy[variable + "_power_" + "(%s)" % p]["Quality(%s)" % label][
                      "Mean quality (%s)" % dbModelingParams['method']])

def mixResults(data, dbModelingParams, dbPowers, mixedVariables, variabMixList, yLabels,
               displayParams=None):  #todo

    """
    Computes results for multiple power combinations of a selected variable
    Order - for 1 unit - iterate through all parameter values - then repeat

    :param mixedVariables:
    :param variabMixList:
    :param dbPowers:
    :param mixVariables:
    :param data:
    :param yLabels:
    :param modelingParams:
    :param displayParams:
    :return:
    """

    variabMixStudy = {"combined variables": mixedVariables, "combinations": variabMixList}
    keys = []
    for listOfCombinations in variabMixList: # listOfCombinations = list of lists
        xSets, ySetsMultiVar, variabLabels = data.asDataframes(dbPowers, listOfCombinations)
        k = "<" + '//'.join(variabLabels) + ">"
        variabMixStudy[k] = scenarioResults(yLabels, xSets, ySetsMultiVar,variabLabels, dbModelingParams)
        keys.append(k)

    if displayParams:
        # mixDisplay(mixedVariables, variabMixList, variabMixStudy, keys, yLabels, dbModelingParams, displayParams)
        studyDisplay(mixedVariables, variabMixList, variabMixStudy, keys, yLabels, dbModelingParams, displayParams,
                      variableText="combined variable :", listText="combinations :")


        if displayParams["archive"]:
            saveStudy(displayParams, variabMixStudy, keys, yLabels, dbModelingParams)

    return variabMixStudy

def mixDisplay(mixedVariables, variabMixList, variabMixStudy, keys, yLabels, dbModelingParams, displayParams): #todo

    if displayParams['showAll']:
        for k, v in variabMixStudy.items():
            print(k, ":", v)
    if displayParams['showAccuracy']:
        print("combined variable :", mixedVariables)
        print("combinations :", variabMixList)
        print("metric:", "Mean quality (%s)" % dbModelingParams['method'])
        for listOfCombinations, key in zip(variabMixList, keys):
            for label in yLabels:

                print(key, label, ":", variabMixStudy[key]["Quality(%s)" % label]["Mean quality (%s)" % dbModelingParams['method']])

def studyDisplay(variables, variableList, Result, keys, yLabels, dbModelingParams, displayParams, variableText, listText): #todo

    if displayParams['showAll']:
        for k, v in Result.items():
            print(k, ":", v)
    if displayParams['showAccuracy']:
        print(variableText, variables)
        print(listText, variableList)
        print("metric:", "Mean quality (%s)" % dbModelingParams['method'])
        for key in keys:
            for label in yLabels:
                print(key, "(%s)" % label, ":", Result[key]["Quality(%s)" % label]["Mean quality (%s)" % dbModelingParams['method']])

def saveStudy(displayParams, Results, keys = None, yLabels=None, dbModelingParams=None):

    import os
    if not os.path.isdir(displayParams["outputPath"]):
        os.makedirs(displayParams["outputPath"])

    with open(displayParams["outputPath"] + displayParams["reference"] + ".txt", 'a') as f:
        print("RESULTS ", file=f)
        print('', file=f)
        if keys and displayParams['showAccuracy']:
            print("RECAP -", "Mean quality (%s)" % dbModelingParams['method'],  file=f)
            print('', file=f)
            for key in keys:
                for label in yLabels:
                   print(key, label, ":", Results[key]["Quality(%s)" % label]["Mean quality (%s)" % dbModelingParams['method']], file=f)
            print('', file=f)
        if displayParams['showAll']:
            print("DETAIL", file=f)
            print('', file=f)
            for ks, vs in Results.items():
                if type(vs) == dict:
                    print(">", ks, ':', file=f)
                    counts = 1
                    for k, v in vs.items():
                        print("   ", ".", k, ":", v, file=f)
                    print('', file=f)
                else:
                    print(">", ks, ":", vs, file=f)
                    print('', file=f)

    f.close()