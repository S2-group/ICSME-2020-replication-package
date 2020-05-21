import sys
import numpy
import pandas
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn
import matplotlib.patches as mpatches

metricNames = {
    'first-contentful-paint': 'FCP',
    'first-meaningful-paint': 'FMP',
    'speed-index': 'SI',
    'total-blocking-time': 'TBT',
    'estimated-input-latency': 'EIL',
    'first-cpu-idle': 'FCI',
    'time-to-interactive': 'TTI',
    'network-requests': 'NR',
    'dom-size': 'DOM',
    'lowest-time-to-widget': 'LTTW',
    'median-time-to-widget': 'MTTW',
}

subjects = [
    'LightBase',
    'LightLoader',
    'ImageBase',
    'ImageLoader',
    'HeavyBase',
    'HeavyLoader'
]

# Returns a seaborn scatterplot


def generateScatter(Data, ax):
    return seaborn.stripplot(data=Data, color='#4FC1F8', ax=ax)


def generateBoxenPlot(Data, ax):
    return seaborn.boxenplot(data=Data, color='#554FC1F8', ax=ax)


def generateMetricPoints(Data, ax):
    for i in range(0, 6):
        ax.plot(i, metrics[i], color='#B943FF', marker='*')


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('This script requires you to specify two .csv files as input. Please do so.')
        exit(1)

    Data1 = pandas.read_csv(sys.argv[1], header=0)
    Data2 = pandas.read_csv(sys.argv[2])

    fig, axs = plt.subplots(int(len(metricNames) / 3) + 1,
                            3, figsize=((3 * 8, int(len(metricNames) / 3) * 5)))
    index = 0
    for column in Data1:
        metrics = Data1[column].to_numpy()
        users = numpy.asarray(Data2.median(axis=0))

        if metrics[0] != 0 and column in metricNames:
            rowIndex = int(index / 3)
            columnIndex = int(index % 3)
            ax = axs[rowIndex, columnIndex]

            plot = generateScatter(Data2, ax)

            generateMetricPoints(Data1, ax)

            # Draw best fit lines
            print('row: ' + str(rowIndex) + ' col: ' + str(columnIndex))
            ax.plot(numpy.poly1d(numpy.polyfit([1, 2, 3, 4, 5, 6], metrics, 1))(
                numpy.unique([1, 2, 3, 4, 5, 6])), color='#B943FF', linewidth=1)
            ax.plot(numpy.poly1d(numpy.polyfit([1, 2, 3, 4, 5, 6], users, 1))(
                numpy.unique([1, 2, 3, 4, 5, 6])), color='black', linewidth=1)

            # Need to help matplotlib with the legend
            metricsLegend = mpatches.Patch(
                color='#B943FF', label=metricNames[column])
            userLegend = mpatches.Patch(color='#4FC1F8', label='uPLT')
            ax.legend(
                handles=[metricsLegend, userLegend])

            ax.set(xlabel='Videos', ylabel='Time (ms)',)
            # ax.xlabel('Videos')
            # ax.ylabel('Time (ms)')
            # ax.set_xticks([0, 1, 2, 3, 4, 5], subjects)
            ax.set_ylim([0, 12000])
            ax.set_xticklabels(subjects, fontdict=None, minor=False)

            index += 1

    fig.tight_layout()
    fig.savefig('results/' + column + '.png')
    fig.clf()

    print('Done!')
