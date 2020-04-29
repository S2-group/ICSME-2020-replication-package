import sys
import numpy
import pandas
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn
import matplotlib.patches as mpatches

metricNames = {
    'first-contentful-paint': 'First Contenful Paint',
    'first-meaningful-paint': 'First Meaningful Paint',
    'speed-index': 'Speed Index',
    'total-blocking-time': 'Total Blocking Time',
    'estimated-input-latency': 'Estimated Input Latency',
    'first-cpu-idle': 'First CPU Idle',
    'time-to-interactive': 'Time to Interactive',
    'network-requests': 'Network Requests',
    'dom-size': 'DOM Size',
    'lowest-time-to-widget': 'Lowest Time to Widget',
    'median-time-to-widget': 'Median Time to Widget',
}

# Returns a seaborn scatterplot
def generateScatter(Data):
    return seaborn.stripplot(data=Data, color='#4FC1F8')

def generateBoxenPlot(Data):
    return seaborn.boxenplot(data=Data, color='#554FC1F8')

def generateMetricPoints(Data):
            for i in range(0, 6):
                plt.plot(i, metrics[i], color='#B943FF', marker='*')


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('This script requires you to specify two .csv files as input. Please do so.')
        exit(1)

    Data1 = pandas.read_csv(sys.argv[1], header=0)
    Data2 = pandas.read_csv(sys.argv[2])

    for column in Data1:
        metrics = Data1[column].to_numpy()
        users = numpy.asarray(Data2.median(axis=0))
        
        if metrics[0] != 0 and column in metricNames:
            plot = generateScatter(Data2)

            generateMetricPoints(Data1)

            # Draw best fit lines
            plt.plot(numpy.poly1d(numpy.polyfit([1, 2, 3, 4, 5, 6], metrics, 1))(numpy.unique([1, 2, 3, 4, 5, 6])), color='#B943FF', linewidth=1)
            plt.plot(numpy.poly1d(numpy.polyfit([1, 2, 3, 4, 5, 6], users, 1))(numpy.unique([1, 2, 3, 4, 5, 6])), color='black', linewidth=1)

            
            # Need to help matplotlib with the legend
            metricsLegend = mpatches.Patch(color='#B943FF', label=metricNames[column])
            userLegend = mpatches.Patch(color='#4FC1F8', label='uPLT')
            plt.legend(handles=[metricsLegend, userLegend])

            plt.xlabel('Videos')
            plt.ylabel('Time (ms)')
            plt.xticks([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
            plt.ylim(0, 12000)
            figure = plot.get_figure()

            figure.tight_layout()
            figure.savefig('results/' + column + '.png')
            figure.clf()
            plt.close()
        
    print('Done!')
