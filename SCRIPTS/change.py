def scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar):
    # todo:

    Results = {"Modelling Parameters": modelingParams}
    for i in range(len(yLabels)):
        ySets = [batch[:, i] for batch in ySetsMultiVar]
        score, theta, scores = rotation(xSets, ySets, modelingParams)
        Results["Quality(%s)" % yLabels[i]] = {"Mean quality (%s)" % modelingParams['method']: score,
                                               "Batchs quality (%s)" % modelingParams['method']: scores}
        Results["Theta(%s)" % yLabels[i]] = {"Theta - labels": variabLabels,
                                             "Theta - first(%s)" % len(theta[0]): theta[0],
                                             "Theta - mean": np.array([np.mean(theta, axis=0)]),
                                             "Theta - std ": np.array([np.std(theta, axis=0)]),
                                             "Theta (%s)" % [len(theta), len(theta[0])]: theta}

    return Results


def scenarioDisplay(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar, displayParams):
    import os
    Results = scenarioResults(yLabels, variabLabels, xSets, modelingParams, ySetsMultiVar)
    for i in range(len(yLabels)):

        if displayParams["showAccuracy"]:
            print("Evaluation(%s) -" % yLabels[i], "Mean quality (%s) :" % modelingParams['method'],
                  Results["Quality(%s)" % yLabels[i]]["Mean quality (%s)" % modelingParams['method']])
        if displayParams["showThetas"]:
            for k in range(len(theta[0])):
                print(Results["Theta(%s)" % yLabels[i]]["Theta - labels"][k],
                      Results["Theta(%s)" % yLabels[i]]["Theta - mean"][:, k])
            print()
    if displayParams["showAll"]:
        for ks, vs in Results.items():
            print(ks, ':')
            for k, v in vs.items():
                print(k, ":", v)
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