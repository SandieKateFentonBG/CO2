def scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams):
    import os
    #todo: s^plit this into resuts and display

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

    return Results




def scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams):
    import os
    #todo: s^plit this into resuts and display

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

        return Results

def scenarioDisplay(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams):
    Results = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams)
    for i in range(len(yLabels)):
        if displayParams["showAccuracy"]:
            print("Evaluation(%s) -" % yLabels[i], "Mean quality (%s) :" % modelingParams['method'], Results["Quality(%s)" % yLabels[i]] ["Mean quality (%s)" % modelingParams['method']])
        if displayParams["showThetas"]:
            for k in range(len(theta[0])):
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

    return Results



def scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams):
    import os
    #todo: s^plit this into resuts and display

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

        if displayParams["showAccuracy"]:
            print("Evaluation(%s) -" % yLabels[i], "Mean quality (%s) :" % modelingParams['method'], Results["Quality(%s)" % yLabels[i]] ["Mean quality (%s)" % modelingParams['method']])
        print(len(Results["Theta(%s)" % yLabels[i]]["Theta - labels"]))
        print(len(theta[0]))
        print(len(Results["Theta(%s)" % yLabels[i]]["Theta - labels"])==len(theta[0]))
        if displayParams["showThetas"]:
            for k in range(len(theta[0])):
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

    return Results

def studyParam():


    paramStudy = {"studied parameter": modelingParamsKey, "parameter values": paramList}
    for i in range(len(yLabels)):
        key = '%s' % modelingParams['method'] + '(%s)' % yLabels[i]
        paramStudy[key] = []
        for elem in paramList:
            modelingParams[modelingParamsKey] = elem

            regResults = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams)
            paramStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']])

    return paramStudy


def scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams = None):

    """
    Computes results for 1 single scenario

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
    return Results


def scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams=None):
    """
    Computes results for 1 single scenario

    :param yLabels: unit studied
    :param variabLabels: variables in the hypothesis function
    :param xSets: sets used for cross validation
    :param modelingParams: model parameters
    :param ySetsMultiVar: target sets including all studied units
    :return:
    """

    for i in range(len(yLabels)):
        ySets = [batch[:, i] for batch in ySetsMultiVar]
        Results = singleResults(yLabels, variabLabels, xSets, ySets, modelingParams)

    if displayParams:
        scenarioDisplay(Results, yLabels, modelingParams, displayParams)

    return Results


def singleResults(yLabels, variabLabels, xSets, ySets, modelingParams):
    Results = {"Modelling Parameters": modelingParams}

    score, theta, scores = rotation(xSets, ySets, modelingParams)
    Results["Quality(%s)" % yLabels] = {"Mean quality (%s)" % modelingParams['method']: score,
                                        "Batchs quality (%s)" % modelingParams['method']: scores}
    Results["Theta(%s)" % yLabels] = {"Theta - labels": variabLabels, "Theta - first(%s)" % len(theta[0]): theta[0],
                                      "Theta - mean": np.array([np.mean(theta, axis=0)]),
                                      "Theta - std ": np.array([np.std(theta, axis=0)]),
                                      "Theta (%s)" % [len(theta), len(theta[0])]: theta}

    return Results




def studyParam(paramList, yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar,  modelingParamsKey, displayParams =  None):

    """
    Computes results for multiple values of a selected parameter
    Order - for 1 unit - iterate through all parameter values - then repeat

    :param paramList:
    :param yLabels:
    :param variabLabels:
    :param xSets:
    :param modelingParams:
    :param ySetsMultiVar:
    :param displayParams:
    :param modelingParamsKey:
    :return:
    """

    paramStudy = {"studied parameter": modelingParamsKey, "parameter values": paramList}
    for i in range(len(yLabels)):
        print("scenario", yLabels[i])
        key = '%s' % modelingParams['method'] + '(%s)' % yLabels[i]
        paramStudy[key] = []
        for elem in paramList:
            modelingParams[modelingParamsKey] = elem
            regResults = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams)
            paramStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']])
    if displayParams:
        for k, v in paramStudy.items():
            print(k,":", v)

    return paramStudy


def studyVariabPower(variable, powerList, powers, mixVariables, data, yLabels, modelingParams, displayParams):

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

    for i in range(len(yLabels)):
        #for CO2e
        key = '%s' % modelingParams['method'] + '(%s)' % yLabels[i] #+ '(%s)' % p
        variabPowerStudy[key] = []
        for p in powerList:
            powers[variable] = p
            print(variable)
            print(powers)
            print(powers[variable])
            # Construct Dataframe with this power p: All X - All y
            x, y, variabLabels = data.asDataframe(powers, mixVariables)
            xSets, ySetsMultiVar = data.asDataframes(powers, mixVariables)

            # for elem in paramList:
            #     modelingParams[modelingParamsKey] = elem
            regResults = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams)
            variabPowerStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']]) #TODO : variabstudy[key] should move
            # variabPowerStudy[key].append(regResults["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']]) #TODO : variabstudy[key] should move

        fullStudy[key] = regResults



    return variabPowerStudy, fullStudy