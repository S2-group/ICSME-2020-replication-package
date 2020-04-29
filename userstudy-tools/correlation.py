import sys
import numpy
import pandas
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn
import matplotlib.patches as mpatches

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('This script requires you to specify two .csv files as input. Please do so.')
        exit(1)

    Data1 = pandas.read_csv(sys.argv[1], header=0)
    Data2 = pandas.read_csv(sys.argv[2])

    i = 0

    for column in Data1:
        metrics = Data1[column].to_numpy()
        users = numpy.asarray(Data2.median(axis=0))
        
        if metrics[0] != 0:
            print(column + ': ' + str(pearsonr(metrics, Data2.median(axis=0))))
            plot = seaborn.scatterplot(data=[metrics, users], legend='brief')

            plt.plot(numpy.poly1d(numpy.polyfit([1, 2, 3, 4, 5, 6], metrics, 1))(numpy.unique([1, 2, 3, 4, 5, 6])), color='#4c72b0')
            plt.plot(numpy.poly1d(numpy.polyfit([1, 2, 3, 4, 5, 6], users, 1))(numpy.unique([1, 2, 3, 4, 5, 6])), color='#dd8452')

            blue_patch = mpatches.Patch(color='#4c72b0', label=column)
            orange_patch = mpatches.Patch(color='#dd8452', label='Median of uPLT')

            plt.legend(handles=[blue_patch, orange_patch])
            plt.xlabel('Videos')
            plt.ylabel('Time (ms)')
            plt.xticks([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
            plt.ylim(0, 12000)
            figure = plot.get_figure()
            figure.savefig('results/' + column + '.png')
            figure.clf()
            plt.close()

    print('Done!')
