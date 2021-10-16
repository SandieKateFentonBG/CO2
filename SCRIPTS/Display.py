
def assessTheta(theta, possibleQualities, powers):
    tLabels = thetaLabelsFlat(possibleQualities, powers)
    for label, value in zip(tLabels, theta):
        print(label, value)

def thetaLabels(possibleQualities, powers):

    thetaLabels = dict(possibleQualities)
    thetaLabels.update(powers)
    return thetaLabels

def thetaValues(thetaOpt,possibleQualities, powers):
    tLabels = thetaLabels(possibleQualities, powers)
    thetaValues = dict()
    index = 0
    for k, v in tLabels.items():
        thetaValues[k] = thetaOpt[index:index+len(v)]
        index += len(v)
    return thetaValues

def thetaAbsMean(thetaValues):
    import numpy as np
    thetaAverages = dict()
    for k, v in thetaValues.items():
        thetaAverages[k]=np.mean(abs(v))
    return thetaAverages

def thetaLabelsFlat(possibleQualities, powers):
    thetaLabels = []
    #gather qualitative labels
    for k, v in possibleQualities.items():
        for value in v:
            qlLabel = k + '_' + value
            thetaLabels.append(qlLabel)
    #gather quantitative labels
    for k, v in powers.items():
        for value in v:
            qtLabel = k + '_exp' + str(value)
            thetaLabels.append(qtLabel)

    return thetaLabels

def thetaLabelsGrafted(possibleQualities, powers, flattened = True):
    thetaLabels = []
    #gather qualitative labels
    for k, v in possibleQualities.items():
        qlLabels = []
        for value in v:
            qlLabel = k + '_' + value
            qlLabels.append(qlLabel)
        thetaLabels.append(qlLabels)
    #gather quantitative labels
    for k, v in powers.items():
        qtLabels = []
        for value in v:
            qtLabel = k + '_exp' + str(value)
            qtLabels.append(qtLabel)
        thetaLabels.append(qtLabels)

    return thetaLabels