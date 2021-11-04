

def plotLoss(loss_a, loss_b, label_a, label_b, title = None, output_path = None, VISU = False):
    import matplotlib.pyplot as plt
    #Display results
    plt.figure()
    plt.plot(loss_a, label=label_a)
    plt.plot(loss_b, label=label_b)
    plt.title(title)
    plt.ylabel(label_b)
    plt.xlabel(label_a)
    plt.legend()
    if output_path :
        plt.savefig(output_path + title + '.png')
    if VISU:
        plt.show()

    plt.close()  # todo : check this

def plotGraph(xList, yList, xLabel, yLabel, displayParams, title=None, figure_size=(8, 10), convertxList=False,
              folder ='visualizetResults'):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    if convertxList:
        xList = [str(elem) for elem in xList]

    df = pd.DataFrame(list(zip(xList, yList)), columns =[xLabel, yLabel])
    fig, ax = plt.subplots(figsize=figure_size)
    if not title :
        title = yLabel + ' as a function of ' + xLabel
    ax.set_title(title)

    if convertxList:
        labels = [str(elem) for elem in xList]
        x = np.arange(len(labels))
        ax.set_ylabel(yLabel)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        plt.setp(ax.get_xticklabels(), rotation=25, ha="right",
                 rotation_mode="anchor")
    sns.scatterplot(data=df, x=xLabel, y=yLabel, hue=yLabel, ax=ax)

    if displayParams['archive']:
        import os
        outputFigPath = displayParams["outputPath"] + '/' + folder

        if not os.path.isdir(outputFigPath):
            os.makedirs(outputFigPath)

        plt.savefig(outputFigPath + '/' + xLabel + '-' + yLabel + '.png')

    if displayParams['showPlot']:
        plt.show()

    plt.close()  # todo : check this


