from ModelAssessment import rotation
import numpy as np


def scenarioResults(yLabels, data, powers, mixVariables, modelingParams, displayParams = None):

    """
    Computes results for 1 single scenario including all ylabels

    :param yLabels: unit studied
    :param variabLabels: variables in the hypothesis function
    :param xSets: sets used for cross validation
    :param modelingParams: model parameters
    :param ySetsMultiVar: target sets including all studied units
    :return:
    """
    x, y, variabLabels = data.asDataframe(powers, mixVariables)
    xSets, ySetsMultiVar = data.asDataframes(powers, mixVariables)

    Results = {"Modelling Parameters": modelingParams}
    for i in range(len(yLabels)):
        print("scenario", yLabels[i])
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
    return Results



def scenarioDisplay(Results, yLabels, modelingParams, displayParams):

    """
    Displays results for 1 single scenario including all ylabels

    :param yLabels: unit studied
    :param modelingParams: model parameters
    :param displayParams: display parameters
    :return: Displays results of 1 scenario
    """

    import os
    # Results = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar)
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

    if displayParams["archive"] and not os.path.isdir(displayParams["outputPath"]):
        os.makedirs(displayParams["outputPath"])

    with open(displayParams["outputPath"] + displayParams["reference"] + ".txt", 'a') as f:
        print("RESULTS ", file=f)
        print('', file=f)
        for ks, vs in Results.items():
            print(ks, ':', file=f)
            for k, v in vs.items():
                print(k, ":", v, file=f)
            print('', file=f)
    f.close()

    # return Results


def studyParam(paramList, yLabels, variabLabels, xSets, dbModelingParams, ySetsMultiVar, modelingParamsKey, displayParams =  None):#todo : change here

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
        paramStudy[modelingParamsKey + "(%s)" % elem] = scenarioResults(yLabels, data, powers, mixVariables, modelingParams, displayParams)#todo : change here
    if displayParams:
        for k, v in paramStudy.items():
            print(k,":", v)

    return paramStudy

def studyVariabPower(variable, powerList, dbPowers,yLabels, variabLabels, xSets, dbModelingParams, ySetsMultiVar, displayParams):

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
    :param powerList:
    :param dbPowers:
    :param mixVariables:
    :param data:
    :param yLabels:
    :param modelingParams:
    :param displayParams:
    :return:
    """

    variabPowerStudy = {"studied variable": variable, "power values": powerList}
    for p in powerList:
        dbPowers[variable] = p #is a list < might not work
        variabPowerStudy[variable + "_power_(" + "(%s)" % p + ")"]= scenarioResults(yLabels, variabLabels, xSets, dbModelingParams, ySetsMultiVar, displayParams)

    if displayParams:
        for k, v in variabPowerStudy.items():
            print(k,":", v)

    return variabPowerStudy




    return variabPowerStudy, fullStudy


def xstudyVariabPower(variable, powerList, powers, mixVariables, data, yLabels, modelingParams, displayParams):

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
    :param powerList:
    :param powers:
    :param mixVariables:
    :param data:
    :param yLabels:
    :param modelingParams:
    :param displayParams:
    :return:
    """

    variabPowerStudy = {"studied variable": variable, "power values": powerList}
    fullStudy = dict()
    for p in powerList:
        powers[variable] = p
        #Construct Dataframe : All X - All y
        x, y, variabLabels = data.asDataframe(powers, mixVariables)
        xSets, ySetsMultiVar = data.asDataframes(powers, mixVariables)
        #
        for i in range(len(yLabels)):
            #for CO2e
            key = '%s' % modelingParams['method'] + '(%s)' % yLabels[i] #+ '(%s)' % p
            variabPowerStudy[key] = []
            # for elem in paramList:
            #     modelingParams[modelingParamsKey] = elem
            regResults = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams)
            variabPowerStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']]) #TODO : variabstudy[key] should move
            # variabPowerStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']]) #TODO : variabstudy[key] should move

            fullStudy[key] = regResults



    return variabPowerStudy, fullStudy