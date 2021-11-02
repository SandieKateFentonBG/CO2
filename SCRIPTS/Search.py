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
    for elem in paramList:
        dbModelingParams[modelingParamsKey] = elem
        paramStudy[modelingParamsKey + "(%s)" % elem] = scenarioResults(yLabels, xSets, ySetsMultiVar, variabLabels, dbModelingParams)#todo : change here

    if displayParams:
        paramDisplay(paramStudy, yLabels, paramList, dbModelingParams, modelingParamsKey, displayParams)

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

    # variabPowerStudy = {"studied variable": variable, "power values": powerList}
    # fullStudy = dict()
    # for i in range(len(yLabels)):
    #     key = '%s' % modelingParams['method'] + '(%s)' % yLabels[i]  # + '(%s)' % p
    #     variabPowerStudy[key] = []
    #     for p in powerList:
    #         powers[variable] = p
    #         x, y, variabLabels = data.asDataframe(powers, mixVariables)
    #         xSets, ySetsMultiVar = data.asDataframes(powers, mixVariables)
    #
    #         # for elem in paramList:
    #         #     modelingParams[modelingParamsKey] = elem
    #         regResults = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams)
    #         variabPowerStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']]) #TODO : variabstudy[key] should move
    #         # variabPowerStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']]) #TODO : variabstudy[key] should move
    #
    #         fullStudy[key] = regResults

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
    for p in variabPowerList:

        xSets, ySetsMultiVar, variabLabels = scenarioDataframe(data, dbPowers, dbMixVariables)

        dbPowers[variable] = p #is a list < might not work

        variabPowerStudy[variable + "_power_" + "(%s)" % p]= scenarioResults(yLabels, xSets, ySetsMultiVar,variabLabels, dbModelingParams)

    if displayParams:
        powerDisplay(variable, variabPowerList, variabPowerStudy, yLabels, dbModelingParams, displayParams)

        if displayParams["archive"]:
            saveStudy(displayParams, variabPowerStudy)

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

def saveStudy(displayParams, Results):

    import os
    if not os.path.isdir(displayParams["outputPath"]):
        os.makedirs(displayParams["outputPath"])

    with open(displayParams["outputPath"] + displayParams["reference"] + ".txt", 'a') as f:
        print("RESULTS ", file=f)
        print('', file=f)
        for ks, vs in Results.items():
            if type(vs) == dict:
                print(ks, ':', file=f)
                for k, v in vs.items():
                    print(k, ":", v, file=f)
                print('', file=f)
            else:
                print(ks, ":", vs, file=f)
                print('', file=f)

    f.close()


def mixResults(): #todo
    pass

def mixDisplay(): #todo
    pass