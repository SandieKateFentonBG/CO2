def plot_results(loss_a, loss_b, label_a, label_b, title = None, output_path = None, VISU = False):
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


def plotGraph(x_list, y_list, x_label, y_label, displayParams, title=None, figure_size=(12, 15), plot=False):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.DataFrame(list(zip(x_list, y_list)), columns =[x_label, y_label])
    fig, ax = plt.subplots(figsize=figure_size)
    if not title :
        title = y_label + ' as a function of ' + x_label
    ax.set_title(title)
    sns.scatterplot(data=df, x=x_label, y=y_label, hue=y_label)
    if displayParams['archive'] :
        import os
        if not os.path.isdir(displayParams["outputPath"]):
            os.makedirs(displayParams["outputPath"])

        plt.savefig(displayParams["outputPath"] + x_label + '-' + y_label +'.png')

    if plot:
        plt.show()

